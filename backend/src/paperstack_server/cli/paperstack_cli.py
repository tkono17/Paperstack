import logging
import typer
import pathlib
from app_basics import getApp
from .document import app as document_app
#from app_basics import app as db_app
from .. import config

logger = logging.getLogger(__name__)
app = typer.Typer()

@app.command('init')
def init_db():
    log.info('Initialize database')
    sApp = getApp()
    #sApp.db.createTables()
    pass

@app.command('reset')
def reset_db():
    log.info('Reset database')
    init_db()
    pass

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    
    app.add_typer(document_app, name='document')
    #app.add_typer(docType.app, name='docType')
    #app.add_typer(docCollection.app, name='docCollection')
    app.add_typer(db_app, name='db')
    app()
    
if __name__ == '__main__':
    main()
    
