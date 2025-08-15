import logging

from ..utils import getUtils
from ..model import Document, DocumentPublic, DocumentCreate, DocumentUpdate
from .base import app, SessionDep

log = logging.getLogger(__name__)

@app.post('/docType/{dt}')
def createDocType(dt: DocTypeCreate, session: SessionDep):
    dt_db = DocType.model_validate(dt)
    session.add(dt_db)
    session.commit()
    session.refresh(dt_db)
    return dt_db

@app.get('/docType/{dt_id')
def getDocType(dt_id: int, session: SessionDep):
    doc = None
    return doc

