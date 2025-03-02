from pathlib import Path
import typer
from typing import Annotated, List

from . import db
from . import main

from models import DocType, DocTypePublic, DocTypeCreate, DocTypeUpdate
from models import Document, DocumentPublic, DocumentCreate, DocumentUpdate
from models import DocCollection, DocCollectionPublic, DocCollectionCreate, DocCollectionUpdate

app = typer.Typer()

documentList: dict[int, DocumentPublic] = {}

@app.command()
def create_document(name: str,
                    title: str | None = None,
                    authors: List[str] = [],
                    filePath: Path | None = None):
    data = DocumentCreate(name=name,
                          title=title,
                          authors=authors,
                          filePath=filePath)
    doc = main.create_document(data)

    documentList[doc_id] = doc
    return doc

if __name__ == '__main__':
    db.on_startup()
    app()
