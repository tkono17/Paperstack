import logging
import typer
from typing import List, Optional
from pathlib import Path
import shutil

from ..app import getApp
from ..model import Document, DocumentPublic, DocumentCreate, DocumentUpdate
from ..model import PaperstackSettings
from .. import api

document_app = typer.Typer()
log = logging.getLogger(__name__)

def createFile(filePath: Path, settings: PaperstackSettings):
    if filePath.exists() and filePath.is_file():
        fp2 = Path(settings.filesDir)/filePath.name
        shutil.copy2(filePath, fp2)
    pass

@document_app.command('create')
def createDocument(name: str,
                   authors: Optional[str] = None,
                   title: Optional[str]         = None,
                   doctype: Optional[str] = None,
                   file_path: Optional[Path]    = None,
                   tags: Optional[List[str]]    = None,
                   eprint: Optional[str]        = None,
                   doi: Optional[str]           = None,
                   citation: Optional[str]      = None,
                   url: Optional[str]           = None,
                   config_file: Optional[Path] = None) -> DocumentPublic:
    app = getApp()
    log.info(f'settings = {app.settings}')

    base_file_path = None
    if file_path is not None and file_path.is_file():
        base_file_path = file_path.name
        createFile(file_path, app.settings)
    doctype_id = None
    doc = DocumentCreate(name=name,
                         authors=authors,
                         title=title,
                         doctype_id=doctype_id,
                         file_path=base_file_path,
                         tags=tags,
                         eprint=eprint,
                         doi=doi,
                         citation=citation,
                         url=url)
    session = next(app.db.getSession())
    return api.createDocument(doc, session)


@document_app.command('get')
def getDocument(doc_id: int,
                configFile: Path = None) -> DocumentPublic:
    if config_file is None:
        config_file = defaultConfigFile()
    readConfig(configFile)

    db = DbAccess.get(setting.sqliteUrl)
    session = next(db.getSession())
    return api.getDocument(doc_id, session)

@document_app.command('update')
def updateDocument(id: int,
                   name: Optional[str]          = None,
                   authors: Optional[List[str]] = None,
                   title: Optional[str]         = None,
                   doctype_id: Optional[str] = None,
                   file_path: Optional[str]     = None,
                   tags: Optional[List[str]]    = None,
                   eprint: Optional[str]        = None,
                   doi: Optional[str]           = None,
                   citation: Optional[str]      = None,
                   url: Optional[str]           = None,
                   configFile: Optional[Path] = None) -> DocumentPublic:
    if config_file is None:
        config_file = defaultConfigFile()
    readConfig(configFile)

    db = DbAccess.get(setting.sqliteUrl)
    session = next(db.getSession())
    return api.getDocument(doc_id, session)

@document_app.command('delete')
def deleteDocument(doc_id: int,
                   configFile: Optional[Path] = None):
    if config_file is None:
        config_file = defaultConfigFile()
    readConfig(configFile)

    db = DbAccess.get(setting.sqliteUrl)
    session = next(db.getSession())
    return api.deleteDocument(doc_id, session)

