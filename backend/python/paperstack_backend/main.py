from fastapi import FastAPI, HTTPException
from models import DocType, DocTypePublic, DocTypeCreate, DocTypeUpdate
from models import Document, DocumentPublic, DocumentCreate, DocumentUpdate
from models import DocCollection, DocCollectionPublic, DocCollectionCreate, DocCollectionUpdate
from typing import Annotated
from sqlmodel import SQLModel, Session, Depends, create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app = FastAPI()

documentList: dict[int, DocumentPublic] = {}

@app.get('/')
def root():
    return {'message': 'Hello World'}
    
@app.post('/documents/', response_model=DocumentPublic)
def create_document(document: DocumentCreate, session: SessionDep):
    #if doc_name == '':
    #    raise HTTPException(status_code=400, detail='Document name cannot be empty')
    doc_ids = {item.name: item.id if item.id is not None else 0 for item in documentList.values()}
    doc = None
    data = {}

    doc_id = max(documentList.keys()) + 1 if documentList else 0
    data = DocumentCreate(doc_id, 
                          name=None)
    # Properties in the request body
    data['author'] = dataIn.author
    data['title'] = dataIn.title
    data['documentType'] = dataIn.documentType
    data['tags'] = dataIn.tags
    data['doi'] = dataIn.doi
    data['arxivId'] = dataIn.arxivId
    data['reference'] = dataIn.reference
    
    doc = DocumentPublic(name=doc_name, **data)
    documentList[doc_id] = doc
    return {'item': documentList[doc_id]}
