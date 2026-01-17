import typer
import pathlib
import logging

from .db import db_app
from .crud_document import document_app
from .crud_doctype import doctype_app
from .crud_query import query_app

log = logging.getLogger(__name__)

app = typer.Typer()

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')

    app.add_typer(db_app, name='db')
    app.add_typer(document_app, name='document')
    app.add_typer(doctype_app, name='doctype')
    app.add_typer(query_app, name='query')
    app()

if __name__ == '__main__':
    main()
