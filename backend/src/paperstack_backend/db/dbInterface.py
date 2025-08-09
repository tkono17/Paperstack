from sqlmodel import Session, create_engine, SQLModel
from typing import Annotated
from fastapi import Depends
from .. import model
from ..config import setting

engine = None

def connectDb():
    global engine
    dburl = setting.sqliteUrl
    connect_args = {"check_same_thread": False}
    engine = create_engine(dburl, connect_args=connect_args)
    return engine

def get_session():
    global engine
    if engine is None:
        connectDb()
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def create_db_and_tables():
    print(f'create SQL tables')
    global engine
    if engine is None:
        connectDb()
    SQLModel.metadata.create_all(engine)

def on_startup():
    create_db_and_tables()

