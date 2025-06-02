import logging
import typer
from typing import List
from ..model import DocCollectionPublic, DocCollectionCreate, DocCollectionUpdate

logger = logging.getLogger(__name__)

app = typer.Typer()

@app.command('create')
def createDocCollection(name: str,
                  log_level: str = 'INFO'):
    logger.debug('Create DocCollection {data}')

@app.command('get')
def getDocCollection(name: str,
                  log_level: str = 'INFO'):
    logger.debug('Get DocCollection {data}')

@app.command('update')
def updateDocCollection(name: str,
                  log_level: str = 'INFO'):
    logger.debug('Update DocCollection {data}')

@app.command('delete')
def deleteDocCollection(name: str,
                  log_level: str = 'INFO'):
    logger.debug('Delete DocCollection {data}')
