from typing import Annotated, Optional, List
from fastapi import Query
from sqlmodel import select
import logging

from ..model import Document, DocumentPublic, DocumentCreate, DocumentUpdate
from ..model import QueryConditionUpdate
from .base import app, SessionDep

log = logging.getLogger(__name__)

@app.post('/document/create')
def createDocument(data: DocumentCreate, session: SessionDep):
    data_db = Document.model_validate(data)
    session.add(data_db)
    session.commit()
    session.refresh(data_db)
    return data_db

@app.post('/document/', response_model=list[DocumentPublic])
def getDocuments(session: SessionDep,
                 conditions: Optional[List[QueryConditionUpdate]] = None, 
                 offset: int = 0,
                 limit: Annotated[int, Query(le=100)] = 100):
    documents = []
    log.info('getDoc')
    if conditions is None:
        statement = select(Document).offset(offset).limit(limit)
        documents = session.exec(statement).all()
    else:
        log.warning('Document read with query not supported yet.')
        log.info(conditions)
        documents = []
    return documents

@app.get('/document/{doc_id}', response_model=DocumentPublic)
def getDocument(doc_id: int, session: SessionDep):
    doc = session.get(Document, doc_id)
    if doc is None:
        raise HTTPException(status_code=404, detail='Document not found')
    return doc

@app.patch('/document/update/{doc_id}', response_model=DocumentPublic)
def updateDocument(doc_id: int,
                   data: DocumentUpdate,
                   session: SessionDep):
    doc_db = session.get(Document, doc_id)
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
    doc_db = session.get(Document, doc_id)
    if doc_db is None:
        raise HTTPException(status_code=404, detail='Document not found')
    session.delete(doc_db)
    session.commit()
    return { 'ok': True }

@app.get('/file/{file_id}')
def getFile(file_id: int):
    return None
