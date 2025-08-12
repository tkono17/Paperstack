import logging
import typer
from typing import List, Optional
from pathlib import Path
import shutil

from ..config import readConfig, defaultConfigFile, setting
from ..model import DocumentPublic, DocumentCreate, DocumentUpdate
from ..api import document
from ..db import DbAccess

app = typer.Typer()
log = logging.getLogger(__name__)

def createFile(filePath: Path):
    if filePath.exists() and filePath.is_file():
        fp2 = Path(setting.filesDir)/filePath.name
        shutil.copy2(filePath, fp2)
    pass

@app.command('create')
def createDocument(name: str,
                   authors: Optional[List[str]] = None,
                   title: Optional[str]         = None,
                   document_type: Optional[str] = None,
                   file_path: Optional[Path]    = None,
                   tags: Optional[List[str]]    = None,
                   eprint: Optional[str]        = None,
                   doi: Optional[str]           = None,
                   citation: Optional[str]      = None,
                   url: Optional[str]           = None,
                   config_file: Optional[Path] = None) -> DocumentPublic:
    if config_file is None:
        config_file = defaultConfigFile()
    readConfig(config_file)
    log.info(f'setting = {setting}')
    
    base_file_path = None
    if file_path is not None and file_path.is_file():
        base_file_path = file_path.name
        createFile(file_path)
    doc = DocumentCreate(name=name,
                         authors=authors,
                         title=title,
                         document_type=document_type,
                         file_path=base_file_path,
                         tags=tags,
                         eprint=eprint,
                         doi=doi,
                         citation=citation,
                         url=url)
    db = DbAccess.get(setting.sqliteUrl)
    session = next(db.getSession())
    return document.createDocument(doc, session)


@app.command('get')
def getDocument(doc_id: int,
                configFile: Path = None) -> DocumentPublic:
    if config_file is None:
        config_file = defaultConfigFile()
    readConfig(configFile)

    db = DbAccess.get(setting.sqliteUrl)
    session = next(db.getSession())
    return document.getDocument(doc_id, session)

@app.command('update')
def updateDocument(id: int,
                   name: Optional[str]          = None,
                   authors: Optional[List[str]] = None,
                   title: Optional[str]         = None,
                   document_type: Optional[str] = None,
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
    return document.getDocument(doc_id, session)

@app.command('delete')
def deleteDocument(doc_id: int,
                   configFile: Optional[Path] = None):
    if config_file is None:
        config_file = defaultConfigFile()
    readConfig(configFile)

    db = DbAccess.get(setting.sqliteUrl)
    session = next(db.getSession())
    return document.deleteDocument(doc_id, session)

