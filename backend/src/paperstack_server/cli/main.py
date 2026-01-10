import typer
import pathlib
import logging
from ..app import getApp
from .db import db_app
from .crud_document import document_app

log = logging.getLogger(__name__)

app = typer.Typer()

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')

    app.add_typer(db_app, name='db')
    app.add_typer(document_app, name='document')
    #app.add_typer(docType.app, name='docType')
    #app.add_typer(docCollection.app, name='docCollection')
    app()
