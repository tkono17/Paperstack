import fastapi
import logging
from ..model import Document, DocumentPublic, DocumentCreate, DocumentUpdate
from ..db import SessionDep
from .. import config

log = logging.getLogger(__name__)

app = fastapi.FastAPI()

@app.post('/document/create')
def createDocument(data: DocumentCreate,
                   session: SessionDep):
    db_doc = Document.model_validate(data)
    log.info(f'Create document {data.name}')
    log.info(f'session = {session}')
    session.add(db_doc)
    session.commit()
    session.refresh(db_doc)
    return db_doc

@app.get('/document/{doc_id}')
def getDocument(doc_id: int, session: SessionDep):
    pass

@app.post('/document/update')
def updateDocument(data: DocumentUpdate, session: SessionDep):
    pass

@app.post('/file/create')
def createFile(data: UploadedFile, session: SessionDep):
    pass

@app.get('/file/{file_id}')
def getFile(file_id: int, session: SessionDep):
    return None

