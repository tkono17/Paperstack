import logging
import typer
from pathlib import Path

from .. import config
from ..db import on_startup, get_session
from .. import api
from .. import model

log = logging.getLogger(__name__)
app = typer.Typer()

@app.command()
def testCrud(config_file: Path | None = None):
    if config_file is None:
        config_file = Path(f'{config}/pstack.db')
    setting = config.readConfig(config_file)
    log.info(f'Setting: {config.setting}')

    session = get_session().__next__()
    log.info(f'session before call: {session}')
    doc = model.DocumentCreate(name='First document')
    
    api.createDocument(doc, session)
    
    on_startup()

def mainTestCrud():
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)-8s %(message)s')
    app()

if __name__ == '__main__':
    mainTestCrud()
    
    
    
