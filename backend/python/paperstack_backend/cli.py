from pathlib import Path
import typer
from typing import Annotated, List

from sqlmodel import Session

from . import db
from . import main

#from .models import DocType, DocTypePublic, DocTypeCreate, DocTypeUpdate
from .models import Document, DocumentPublic, DocumentCreate, DocumentUpdate
#from .models import DocCollection, DocCollectionPublic, DocCollectionCreate, DocCollectionUpdate

app = typer.Typer()

documentList: dict[int, DocumentPublic] = {}

#-----------------------------------------------------------------------
# Database operation
#-----------------------------------------------------------------------
@app.command('initDatabase')
def initDatabase(dbType: str = 'sqlite', 
                 fname: str = 'pstack.db'):
    fpath = Path(fname)
    if fpath.exists():
        print(f'  Database file {fpath} exists. Use another file or delete this file first')
        return
    dbpath = f'sqlite:///{fpath.absolute()}'
    print(f'Initialize database {dbpath}')
    db.connectDatabase(dbpath)
    db.create_db_and_tables()

#-----------------------------------------------------------------------
# Document CRUD
#-----------------------------------------------------------------------
@app.command('createDocument')
def createDocument(name: str,
                    title: str | None = None,
                    authors: List[str] = [],
                    filePath: Path | None = None):
    data = DocumentCreate(name=name,
                          title=title,
                          authors='T. Kono',
                          filePath=filePath,
                          documentType='article',
                          tags='example',
                          arxivId='',
                          doi='',
                          reference='',
                          file=None
    )
    dbi = db.DbInterface.get('sqlite:///pstack.db')
    session = dbi.getSession()
    print(f'  session in cli {session} {session.__class__}')
    doc = main.create_document(data, session)

    #documentList[doc_id] = doc
    return doc

@app.command('readDocuments')
def readDocuments():
    docs =[]
    return docs

if __name__ == '__main__':
    db.on_startup()
    app()
