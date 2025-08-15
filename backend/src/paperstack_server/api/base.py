from sqlmodel import Session
from fastapi import FastAPI, Depends

from ..utils import getUtils

def get_session():
    utils = getUtils()
    if utils is not None and utils.db is not None:
        return utils.db.getSession()
    return None

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

