import fastapi
from sqlmodel import Session, select
from typing import Annotated, List
from ..model import Settings
from ..utils import getUtils
from .base import app

config_file = None
getUtils().init()

@app.get('/')
def root():
    return {'message': 'Hello World'}
    
