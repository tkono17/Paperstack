from sqlmodel import Session, create_engine, SQLModel
from typing import Annotated


sqlite_file_name = "database.db"
dburl = f"sqlite:///{sqlite_file_name}"

class DbInterface:
    s_dbi = None

    @staticmethod
    def get(url=None):
        if DbInterface.s_dbi == None:
            DbInterface.s_dbi = DbInterface(url)
        return DbInterface.s_dbi

    def __init__(self, url):
        self.engine = None
        self.session = None
        self.connect(url)

    def connect(self, url):
        connect_args = {"check_same_thread": False}
        self.engine = create_engine(url, connect_args=connect_args)

    def getSession(self):
        print('In get session')
        with Session(self.engine) as session:
            print(f'before yield: {session}')
            yield session
        print('getSession done')

def connectDatabase(dburl):
    global engine
    connect_args = {"check_same_thread": False}
    engine = create_engine(dburl, connect_args=connect_args)
    return engine

def create_db_and_tables():
    print(f'create SQL tables')
    SQLModel.metadata.create_all(s_dbi.engine)

def get_session():
    pass
    #dbi = db.DbInterface.get()
    #return dbi.getSession()

def on_startup():
    create_db_and_tables()

