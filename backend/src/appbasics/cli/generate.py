import sys
import os
import importlib
import logging
import typer
import typing
import datetime
from pathlib import Path
from dataclasses import _MISSING_TYPE
import dataclasses

log = logging.getLogger(__name__)

app = typer.Typer()

def loadModule(fpath):
    module = None
    if fpath is not None and os.path.exists(fpath):
        dn = os.path.dirname(fpath)
        fn = os.path.basename(fpath)
        idot = fn.find('.')
        mn = fn[:idot] if idot >= 0 else fn
        sys.path.append(dn)
        log.info(f'Import {mn} from {dn}')
        module = importlib.import_module(mn)
    return module

def varType(field):
    tname = None
    if field.type == int:
        tname = 'int'
    elif field.type == float:
        tname = 'float'
    elif field.type == str:
        tname = 'str'
    elif field.type == list:
        tname = field.type
    else:
        tname = field.type
    return tname

def dbType(field):
    tname = str
    log.info(f'py type: {field.type}')
    if field.type == int:
        tname = int

    return db_type

def defaultValue(field):
    dvalue = None
    log.info(f'    {field.name} type:{type(field.type)} value={field.default} valueType: {type(field.default)}')
    match field.default:
        case _: dvalue = field.default
    return dvalue

def isOptional(field):
    if str(field.type).find('Optional')>=0:
        return True
    return False

def isScalar(field):
    result = True
    if field.type == int or field.type == float or field.type == str:
        pass
    elif isOptional(field):
        none_type = type(None)
        for arg in field.type.__args__:
            log.info(f'arg : {arg}')
            if arg not in (int, float, str, none_type):
                log.info(f'  not a scalar')
                result = False
                break
    return result

def isList(field):
    result = False
    if field.default_factory in (list, typing.List):
        result = True
    return result

def isObject(field):
    result = False
    if not (isScalar(field) or isList(field)):
        result = True
    return result

def writeClassBase(cls, fout, baseName=None, prefix=''):
    clsName = cls.__name__
    fout.write(f'{prefix}class {clsName}Base')
    if baseName is not None:
        fout.write(f'({baseName})')
    fout.write(':\n')

    prefix2 = prefix + '  '
    for fieldName, field in cls.__dataclass_fields__.items():
        var_type = varType(field)
        log.info(f'field {fieldName} {dir(field.type)}')
        log.info(f'field {field.type.__name__}')
        fieldString = f'Field(index=True'
        if isOptional(field):
            fieldString += f', default=None'
        fieldString += ')'
        fout.write(f'{prefix2}{field.name}: {var_type} = {fieldString}\n')
    fout.write('\n')

def writeClassDb(cls, fout, baseName=None, prefix=''):
    clsName = cls.__name__
    fout.write(f'{prefix}class {clsName}')
    if baseName is not None:
        fout.write(f'({baseName}, table=True)')
    fout.write(':\n')

    prefix2 = prefix + '  '
    fout.write(f'{prefix2}id: int | None = Field(default=None, primary_key=True)\n')
    for fieldName, field in cls.__dataclass_fields__.items():
        if isList(field):
            pass
        elif isObject(field):
            linkName = f'{fieldName}_id'
            fout.write(f'{prefix2}{linkName}: int | None = Field(default=None, index=True)\n')
    fout.write('\n')

def writeClassPublic(cls, fout, baseName=None, prefix=''):
    clsName = cls.__name__
    fout.write(f'{prefix}class {clsName}Public')
    if baseName is not None:
        fout.write(f'({baseName})')
    fout.write(':\n')

    prefix2 = prefix + '  '
    fout.write(f'{prefix2}id: int | None = field(default=None)\n')
    fout.write('\n')

def writeClassCreate(cls, fout, baseName=None, prefix=''):
    clsName = cls.__name__
    fout.write(f'{prefix}class {clsName}Create')
    if baseName is not None:
        fout.write(f'({baseName})')
    fout.write(':\n')
    prefix2 = prefix + '  '
    fout.write(f'{prefix2}pass\n')
    fout.write('\n')


def writeClassUpdate(cls, fout, baseName=None, prefix=''):
    clsName = cls.__name__
    fout.write(f'{prefix}class {clsName}Update')
    if baseName is not None:
        fout.write(f'({baseName})')
    fout.write(':\n')

    prefix2 = prefix + '  '
    for fieldName, field in cls.__dataclass_fields__.items():
        var_type = varType(field)
        if not isOptional(field):
            var_type = f'{var_type} | None'
        fout.write(f'{prefix2}{field.name}: {var_type} = None\n')
    fout.write('\n')

def generateModel(cls, fout):
    clsName = cls.__name__
    log.info(f'  Generate model for {clsName}')

    fout.write('import typing\n')
    fout.write('from dataclasses import field\n')
    fout.write('from sqlmodel import SQLModel, Field\n')
    fout.write('import basemodel\n')
    fout.write('\n')
    writeClassBase(cls, fout, baseName='SQLModel')
    writeClassDb(cls, fout, baseName=f'{clsName}Base')
    writeClassPublic(cls, fout, baseName=f'{clsName}Base')
    writeClassCreate(cls, fout, baseName=f'{clsName}Base')
    writeClassUpdate(cls, fout, baseName=f'{clsName}Base')

    return None

def generateFastAPI(cls, fout):
    pass

def generateCLI(cls, fout):
    pass

@app.command('all')
def processAll(base_model_file: str,
                 output_dir: str = '.',
                 create_model: bool = True,
                 create_api: bool = True,
                 create_cli: bool = True):
    module = loadModule(base_model_file)

    if module is None:
        log.warning(f'Could not import file {base_model_file}')
    log.info(f'Loaded module {base_model_file}')
    log.info(f'  locals: {dir(module)}')
    dirName = os.path.dirname(base_model_file)
    dirName = os.path.dirname(dirName)

    for sn in dir(module):
        data = getattr(module, sn)
        if data is None or type(data).__name__ != 'type': continue
        clsName = data.__name__
        clsname = clsName.lower()
        log.info(f'Base model in {dirName}')
        log.info(f'  type of {clsName} is {type(data).__name__}')
        log.info(f'  dir => {dir(data)}')

        log.info(f'  annotations => {data.__annotations__}')

        with open(f'{dirName}/model/_{clsname}.py', 'w') as fout:
            generateModel(data, fout)
        #with open(f'{dirName}/model/_{clsname}.py', 'w') as fout:
        #    generateFastAPI(data, fout)
        #with open(f'{dirName}/model/_{clsname}.py', 'w') as fout:
        #    generateCLI(data, fout)
    pass

def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    app()

if __name__ == '__main__':
    main()
