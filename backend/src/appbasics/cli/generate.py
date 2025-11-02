import sys
import os
import importlib
import logging
import typer
from pathlib import Path

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

def generateModel(cls, fout):
    clsName = cls.__name__
    log.info(f'  Generate model for {clsName}')
    for x in dir(cls):
        log.info(f'  {x} -> {getattr(cls, x)}')
    
    fout.write(f'class {clsName}:\n')
    prefix = '  '
    
    for name in cls.__dataclass_fields__:
        annotation = cls.__annotations__[name]
        field = cls.__dataclass_fields__[name]
        tname = annotation
        if annotation in (str, int, float):
            tname = annotation.__name__
        log.info(f'    annotation {name} -> {tname}, {field}')
        fout.write(f'{prefix}{name}: {tname}\n')
    pass

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
