import logging
import typer
from typing import List
from ..model import DocTypePublic, DocTypeCreate, DocTypeUpdate

logger = logging.getLogger(__name__)

app = typer.Typer()

@app.command('create')
def createDocType(name: str,
                  log_level: str = 'INFO'):
    logger.debug('Create DocType {data}')

@app.command('get')
def getDocType(name: str,
                  log_level: str = 'INFO'):
    logger.debug('Get DocType {data}')

@app.command('update')
def updateDocType(name: str,
                  log_level: str = 'INFO'):
    logger.debug('Update DocType {data}')

@app.command('delete')
def deleteDocType(name: str,
                  log_level: str = 'INFO'):
    logger.debug('Delete DocType {data}')
