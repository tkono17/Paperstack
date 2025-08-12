from sqlmodel import Session, create_engine, SQLModel
from typing import Annotated
from fastapi import Depends
import logging

from .. import model
from ..config import setting

log = logging.getLogger(__name__)

class DbAccess:
    sInstance = None

    @classmethod
    def get(cls, url=setting.sqliteUrl):
        x = None
        log.info(f'In DbAccess.get: cls={cls}, instance={cls.sInstance}')
        if cls.sInstance is None:
            log.info(f'  Create DB instance {url}')
            cls.sInstance = cls(url)
        x = cls.sInstance
        log.info(f'DB instance: {x}')
        return x

    def __init__(self, url):
        self.url = url
        self.engine = None

    def connectDb(self):
        connect_args = {
            'check_same_thread': False
        }
        self.engine = create_engine(self.url, connect_args=connect_args)
        return self.engine

    def getSession(self):
        if self.engine is None:
            self.connectDb()
        with Session(self.engine) as session:
            yield session

    def createTables(self):
        if self.engine is None:
            self.connectDb()
        SQLModel.metadata.create_all(self.engine)

def get_session():
    db = DbAccess.get()
    return db.getSession()

SessionDep = Annotated[Session, Depends(get_session)]

def on_startup():
    db = DbAccess.get()
    db.createTables()

