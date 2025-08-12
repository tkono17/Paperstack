import logging
import typer
import pathlib
from .document import app as document_app
from ..db import app as db_app
from .. import config

logger = logging.getLogger(__name__)
app = typer.Typer()

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
    
