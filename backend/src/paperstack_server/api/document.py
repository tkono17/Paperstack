from typing import Annotated, Optional, List
from fastapi import Query, UploadFile
from sqlmodel import select
import logging

from appbasics import DbCrud
from ..model import Document, DocumentPublic, DocumentCreate, DocumentUpdate
from ..model import QueryConditionUpdate
from .base import app, SessionDep

log = logging.getLogger(__name__)

@app.post('/document/create')
def createDocument(data: DocumentCreate, session: SessionDep):
    crud = DbCrud(DocumentPublic, DocumentCreate, DocumentUpdate,
                  Document, session)
    return crud.create(data)

@app.post('/document/', response_model=list[DocumentPublic])
def getDocuments(session: SessionDep,
                 conditions: Optional[list[QueryConditionUpdate]] = None, 
                 offset: int = 0,
                 limit: Annotated[int, Query(le=100)] = 100):
    crud = DbCrud(DocumentPublic, DocumentCreate, DocumentUpdate,
                  Document, session)
    return crud.get(data)

@app.get('/document/{doc_id}', response_model=DocumentPublic)
def getDocument(doc_id: int, session: SessionDep):
    doc = session.get(Document, ObjId(doc_id))
    if doc is None:
        raise HTTPException(status_code=404, detail='Document not found')
    return doc

@app.patch('/document/update/{doc_id}', response_model=DocumentPublic)
def updateDocument(doc_id: int,
                   data: DocumentUpdate,
                   session: SessionDep):
    doc_db = session.get(Document, ObjId(doc_id))
    if doc_db is None:
        raise HTTPException(status_code=404, detail='Document not found')
    doc_data = data.model_dump(exclude_unset=True)
    doc_db.sqlmodel_update(doc_data)
    session.add(doc_db)
    session.commit()
    session.refresh(doc_db)
    return doc_db

@app.delete('/document/{doc_id}')
def deleteDocument(doc_id: int,
                   session: SessionDep):
    doc_db = session.get(Document, ObjId(doc_id))
    if doc_db is None:
        raise HTTPException(status_code=404, detail='Document not found')
    session.delete(doc_db)
    session.commit()
    return { 'ok': True }

@app.post('/file/create')
def createFile(data: UploadFile, session: SessionDep):
    return None

@app.get('/file/{file_id}')
def getFile(file_id: int, session: SessionDep):
    return None

@app.delete('/file/{file_id}')
def deleteFile(file_id: int, session: SessionDep):
    return None
