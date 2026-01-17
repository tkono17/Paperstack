from sqlmodel import Session
from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from appbasics import getUtils

def get_session():
    utils = getUtils()
    if utils is not None and utils.db is not None:
        yield next(utils.db.getSession())


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

origins = [
    "http://localhost:3100",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

