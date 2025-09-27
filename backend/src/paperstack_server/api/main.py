import fastapi
from sqlmodel import Session, select
from typing import Annotated, List
from ..app import getApp
from .base import app
from . import document


getApp().init()

@app.get('/')
def root():
    return {'message': 'Hello World'}
    
