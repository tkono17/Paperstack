import logging
from typing import Optional, List
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

