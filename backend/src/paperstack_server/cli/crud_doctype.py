import logging
import typer
from typing import List, Optional
from pathlib import Path
import shutil

from ..app import getApp
from ..model import DocType, DocTypePublic, DocTypeCreate, DocTypeUpdate
from .. import api

doctype_app = typer.Typer()
log = logging.getLogger(__name__)

@doctype_app.command('create')
def createDocType(name: str):
    doctype = DocTypeCreate(name=name)
    app = getApp()
    session = next(app.db.getSession())
    return api.createDocType(doctype, session)


