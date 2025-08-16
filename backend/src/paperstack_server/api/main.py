import fastapi
from sqlmodel import Session, select
from typing import Annotated, List

from ..utils import getUtils, Settings
from .base import app

config_file = None
Settings.init('PAPERSTACK_CONFIG_FILE', '.paperstack.cfg', config_file)
getUtils().init()

@app.get('/')
def root():
    return {'message': 'Hello World'}
    
