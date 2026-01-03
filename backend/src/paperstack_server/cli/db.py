import logging
import typer
import pathlib
from ..app import getApp
from .crud_document import document_app

log = logging.getLogger(__name__)

db_app = typer.Typer()

@db_app.command('init')
def init_db():
    log.info('Initialize database')
    sApp = getApp()
    sApp.db.createTables()
    pass

@db_app.command('reset')
def reset_db():
    log.info('Reset database')
    init_db()
    pass

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    
    db_app()
    
if __name__ == '__main__':
    main()
    
