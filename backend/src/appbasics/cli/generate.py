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
    vType = str
    intT = type(int)
    floatT = type(float)
    log.info(f'    type of the field.type: {type(field.type)}')
    match field.type:
        case typing._UnionGenericAlias: vType =  str(field.default)
        case _: vType = type(field.type).__name__
    return vType

def dbType(field):
    db_type = str
    log.info(f'py type: {field.type}')
    match field.type:
        case 'str' | 'int' | 'float': db_type = field.type
        case datetime.datetime | datetime.date: db_type = 'str'
        case _: db_type = str
    return db_type

def defaultValue(field):
    dvalue = None
    log.info(f'    {field.name} type:{type(field.type)} value={field.default} valueType: {type(field.default)}')
    match field.default:
        case _: dvalue = field.default
    return dvalue

def isList(field):
    result = False
    if field.default_factory in (list, typing.List):
        result = True
    return result

def writeField(field, fout, prefix=''):
    fout.write(f'{prefix}{field[0]}: {field[1]}\n')

def writeClass(clsName, fields, fout, baseName=None, prefix=''):
    fout.write(f'{prefix}class {clsName}')
    if baseName is not None:
        fout.write(f'({baseName})')
    fout.write(':\n')

    for field in fields:
        writeField(field, fout, prefix+'  ')
    fout.write('\n')

def generateModel(cls, fout):
    clsName = cls.__name__
    log.info(f'  Generate model for {clsName}')
    for x in dir(cls):
        log.info(f'  {x} -> {getattr(cls, x)}')

    fields_base = []
    fields_db = []
    fields_public = []
    fields_create = []
    fields_update = []

    is_option = True
    for name in cls.__dataclass_fields__:
        annotation = cls.__annotations__[name]
        field = cls.__dataclass_fields__[name]

        var_type = varType(field)
        db_type = dbType(field)
        value = defaultValue(field)
        is_list = isList(field)

        value = None
        fields_base.append( (name, var_type, db_type, value,) )
        fields_public.append( (name, var_type, db_type, value) )
        fields_create.append( (name, var_type, db_type, value) )
        fields_update.append( (name, var_type, db_type, None) )
        if not is_list:
            fields_db.append( (name, var_type, db_type, value) )

    fout.write('import typing\n')
    fout.write('from sqlmodel import SQLModel\n')
    fout.write('\n')
    writeClass(f'{clsName}Base', fields_base, fout, baseName='SQLModel')
    writeClass(f'{clsName}', fields_db, fout, baseName=clsName)
    writeClass(f'{clsName}Public', fields_public, fout, baseName=clsName)
    writeClass(f'{clsName}Create', fields_create, fout, baseName=clsName)
    writeClass(f'{clsName}Update', fields_update, fout, baseName=clsName)
    return {
        'name': clsName,
        'fields_base': fields_base,
        'fields_db': fields_db,
        'fields_public': fields_public,
        'fields_create': fields_create,
        'fields_update': fields_update
    }

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
