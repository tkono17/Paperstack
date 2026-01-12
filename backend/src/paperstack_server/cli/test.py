import logging
import typer
import importlib.resources
from pathlib import Path

from ..utils import getUtils, Settings
from .. import api
from .. import config
from .. import model

log = logging.getLogger(__name__)
app = typer.Typer()

@app.command()
def create_tables():
    utils = getUtils()
    utils.db.createTables()

@app.command()
def test_crud():
    utils = getUtils()

    session = next(utils.db.getSession())
    log.info(f'session before call: {session}')

    doc = model.DocumentCreate(name='First document')
    api.createDocument(doc, session)

    doc = model.DocumentCreate(name='2nd document')
    api.createDocument(doc, session)


def mainTestCrud():
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)-8s %(message)s')
    config_file = importlib.resources.files('paperstack_server.config').joinpath('paperstack.cfg')

    log.info(f'Settings.defaultConfigFile : {Settings.defaultConfigFile}')
    Settings.init('PAPERSTACK_CONFIG_FILE', '.paperstack.cfg', config_file)
    getUtils().init()
    log.info(f'Utils: {getUtils().settings}')

    app()

if __name__ == '__main__':
    mainTestCrud()
    
    
    
