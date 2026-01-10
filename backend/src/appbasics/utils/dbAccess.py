from sqlmodel import Session, create_engine, SQLModel
import logging

log = logging.getLogger(__name__)

class DbAccess:
    sInstance = None

    @classmethod
    def get(cls, url=None):
        x = None
        if url is None:
            sApp = getApp()
            url = sApp.settings.sqliteUrl
        if cls.sInstance is None:
            log.info(f'  Create DB instance {url}')
            cls.sInstance = cls(url)
        x = cls.sInstance
        return x

    def __init__(self, url):
        self.url = url
        self.engine = None

    def connectDb(self):
        connect_args = {
            'check_same_thread': False
        }
        log.info(f'Create DB engine for {self.url}')
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

