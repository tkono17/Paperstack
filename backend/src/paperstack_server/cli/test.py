import logging
import typer
from pathlib import Path

from ..utils import getUtils
from .. import api
from .. import config
from .. import model

log = logging.getLogger(__name__)
app = typer.Typer()

@app.command()
def testCrud(config_file: Path | None = None):
    if config_file is None:
        config_file = config / 'paperstack.cfg'
    setting = config.readConfig(config_file)
    log.info(f'Setting: {config.setting}')

    utils = getUtils()
    utils.db.createTables()

    session = next(utils.getSession())
    log.info(f'session before call: {session}')
    doc = model.DocumentCreate(name='First document')
    
    api.createDocument(doc, session)



def mainTestCrud():
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)-8s %(message)s')
    getUtils()
    app()

if __name__ == '__main__':
    mainTestCrud()
    
    
    
