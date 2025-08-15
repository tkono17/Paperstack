import fastapi
from sqlmodel import Session, select
from typing import Annotated, List

from ..utils import getUtils, Settings
from .document import create_document, get_document, update_document, delete_document
from .docType import create_docType, get_docType, update_docType, delete_docType


config_file = None
Settings.init('PAPERSTACK_CONFIG_FILE', '.paperstack.cfg', config_file)
getUtils().init()

@app.get('/')
def root():
    return {'message': 'Hello World'}
    
