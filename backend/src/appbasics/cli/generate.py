import sys
import os
import importlib
import logging
import typer
from pathlib import Path

log = logging.getLogger(__name__)

app = typer.Typer()

def load_module(fpath):
    pass

@app.command('process')
def process(base_model_file: str,
            create_model: bool = True,
            create_api: bool = True,
            create_cli: bool = True):
    module = None
    if base_model_file is not None and os.path.exists(base_model_file):
        dn = os.path.dirname(base_model_file)
        fn = os.path.basename(base_model_file)
        idot = fn.find('.')
        mn = fn[:idot] if idot >= 0 else fn
        sys.path.append(dn)
        log.info(f'Import {mn} from {dn}')
        module = importlib.import_module(mn)
    if module is None:
        log.warning(f'Could not import file {base_model_file}')
    log.info(f'Loaded module {base_model_file}')
    log.info(f'  locals: {dir(module)}')
    for sn in dir(module):
        data = getattr(module, sn)
        log.info(f'  type of {sn} is {type(data).__name__}')
        log.info(f'  {data.__class__.__name__}')
    pass

def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    app()

if __name__ == '__main__':
    main()
