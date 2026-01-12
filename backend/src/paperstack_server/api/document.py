import logging
from sqlmodel import Session
from typing import Annotated
from fastapi import FastAPI, Depends

from ..utils import getUtils, Settings
from ..model import Document, DocumentPublic, DocumentCreate, DocumentUpdate
from .base import app, SessionDep

log = logging.getLogger(__name__)


u = getUtils()
u.init()

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

#@app.post('/file/create')
#def createFile(data: UploadedFile, session: SessionDep):
#    pass

@app.get('/file/{file_id}')
def getFile(file_id: int, session: SessionDep):
    return None

