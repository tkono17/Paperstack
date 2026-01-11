import logging

from appbasics import Store
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
def getDocTypes(session: SessionDep):
    return [ DocTypePublic(name=name, id=id) for name, id in store.nameToId.items()]

@app.get('/doctype/{dt_id}', response_model=DocTypePublic)
def getDocType(dt_id: int, session: SessionDep):
    name = store.idToName[dt_id]
    dt2 = DocTypePublic(name=name, id=dt_id)
    return dt2

