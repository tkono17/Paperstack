from sqlmodel import Session, create_engine, SQLModel
from typing import Annotated


sqlite_file_name = "database.db"
dburl = f"sqlite:///{sqlite_file_name}"

engine = None

def connectDatabase(dburl):
    global engine
    connect_args = {"check_same_thread": False}
    engine = create_engine(dburl, connect_args=connect_args)
    return engine

def create_db_and_tables():
    print(f'create SQL tables')
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def on_startup():
    create_db_and_tables()

