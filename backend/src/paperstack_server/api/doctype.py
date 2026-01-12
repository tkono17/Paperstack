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
def getDocTypes(where: Optional[str], session: SessionDep):
    if where is None:
        statement = select(DocType)
        return session.exec(statement)

@app.get('/doctype/{dt_id}', response_model=DocTypePublic)
def getDocType(dt_id: int, session: SessionDep):
    statement = select(DocType).where(DocType.id == dt_id)
    log.info(f'statement: {statement}')
    results = session.exec(statement)
    return results.one()


