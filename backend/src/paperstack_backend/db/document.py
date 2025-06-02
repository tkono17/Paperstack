import logging
import typer
from typing import List, Optional
from ..model import DocumentPublic, DocumentCreate, DocumentUpdate

logger = logging.getLogger(__name__)

app = typer.Typer()

@app.command('create')
def createDocument(name: str,
                   title: str,
                   authors: Optional[List[str]] = None,
                   document_type: str | None = None,
                   file_path: str | None = None,
                   tags: List[str] | None = None,
                   eprint: str | None = None,
                   doi: str | None = None,
                   reference: str | None = None,
                   log_level: str = 'INFO'):
    authors_str = None,
    tags_str = None
    if authors:
        authors_str = ','.join(authors)
    if tags:
        tags_str = ','.join(tags)
    data = DocumentCreate(name=name, title=title,
                          authors=authors_str,
                          documentType=document_type,
                          filePath=file_path,
                          tags=tags_str,
                          eprint=eprint,
                          doi=doi,
                          reference=reference)
    match log_level:
        case 'INFO': logger.setLevel(logging.INFO)
        case 'DEBUG': logger.setLevel(logging.DEBUG)
    logger.debug(f'Create document: {data}')
    pass

@app.command('update')
def updateDocument(id: int | None = None,
                   name: str | None = None):
    pass
    pass

@app.command('get')
def getDocument(id: int | None = None,
                name: str | None = None):
    pass

@app.command('delete')
def deleteDocument(id: int | None = None,
                   name: str | None = None):
    pass

