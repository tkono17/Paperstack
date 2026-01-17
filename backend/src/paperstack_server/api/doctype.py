import logging
from typing import Optional, List
from fastapi import HTTPException
from sqlmodel import select

from ..model import DocType, DocTypeCreate, DocTypePublic, DocTypeUpdate
from .base import app, SessionDep

log = logging.getLogger(__name__)


@app.post('/doctype/')
def createDocType(dt: DocTypeCreate, session: SessionDep) -> DocTypePublic:
    db_data = DocType.model_validate(dt)
    session.add(db_data)
    session.commit()
    session.refresh(db_data)
    return db_data

@app.get('/doctype/', response_model=list[DocTypePublic])
def getDocTypes(session: SessionDep, where: Optional[str] = None):
    offset: int = 0
    limit: int = 100
    entries: list[DocTypePublic] = []
    log.info('getDocType')
    print('check where', where)
    if where is None:
        statement = select(DocType)
        results = session.exec(statement)
        entries = results.all()
    return entries

@app.get('/doctype/{doctype_id}', response_model=DocTypePublic)
def getDocType(doctype_id: int, session: SessionDep):
    statement = select(DocType).where(DocType.id == doctype_id)
    results = session.exec(statement)
    return results.one()

@app.patch('/doctype/{doctype_id}', response_model=DocTypePublic)
def updateDocType(doctype_id: int, data: DocTypeUpdate, session: SessionDep):
    data_db = session.get(DocType, doctype_id)
    if data_db is None:
        raise HTTPException(status_code=404, detail=f"DocType {doctype_id} not found")
    data_update = data.model_dump(exclude_unset=True)
    data_db.sqlmodel_update(data_update)
    session.add(data_db)
    session.commit()
    session.refresh(data_db)
    return data_db

@app.delete('/doctype/{doctype_id}')
def deleteDocType(doctype_id: int, session: SessionDep):
    data = session.get(DocType, doctype_id)
    if data is None:
        raise HTTPException(status_code=404, detail=f'DocType {doctype_id} not found')
    session.delete(data)
    session.commit()
    return {'ok': True}
