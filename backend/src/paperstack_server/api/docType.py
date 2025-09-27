import logging

from app_basics import Store
from ..model import DocType, DocTypeCreate, DocTypePublic, DocTypeUpdate
from .base import app, SessionDep

log = logging.getLogger(__name__)

store = Store()
store.add('Article', 1)
store.add('Eprint', 2)
store.add('Thesis', 3)
store.add('ThesisD', 4)
store.add('ThesisM', 5)
store.add('ThesisB', 6)
store.add('Presentation', 7)
store.add('Manual', 8)
store.add('Specification', 9)
store.add('Tutorial', 10)
store.add('TechnicalNote', 11)
store.add('Datasheet', 12)
store.add('Review', 13)
store.add('Book', 14)

@app.post('/docType/')
def createDocType(dt: DocTypeCreate, session: SessionDep) -> DocTypePublic:
    #dt_db = DocType.model_validate(dt)
    #session.add(dt_db)
    #session.commit()
    #session.refresh(dt_db)
    dt2 = None
    if store.exists(dt.name):
        dt2 = DocTypePublic(dt.name, store.nameToId[dt.name])
    if x is None:
        n = store.size()
        store.add(dt.name, n+1)
        dt2 = DocTypePublic(dt.name, n+1)
    return dt2

@app.get('/docType/', response_model=list[DocTypePublic])
def getDocTypes(session: SessionDep):
    return [ DocTypePublic(name=name, id=id) for name, id in store.nameToId.items()]

@app.get('/docType/{dt_id}', response_model=DocTypePublic)
def getDocType(dt_id: int, session: SessionDep):
    name = store.idToName[dt_id]
    dt2 = DocTypePublic(name=name, id=dt_id)
    return dt2

