#-----------------------------------------------------------------------
# Application data model
#
# Document (Base, Db, Public, Create, Update)
#-----------------------------------------------------------------------
from enum import Enum
from fastapi import UploadFile
from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

#-----------------------------------------------------
# Document
#-----------------------------------------------------
class DocumentBase(SQLModel):
    name: str                 = Field(index=True)
    authors: str | None       = Field(default=None, index=True)
    title: str | None         = Field(default=None, index=True)
    document_type: int | None = Field(default=None, index=True)
    file_path: str | None     = Field(default=None, index=True)
    tags: str | None          = Field(default=None, index=True)
    eprint: str | None        = Field(default=None, index=True)
    doi: str | None           = Field(default=None, index=True)
    citation: str | None      = Field(default=None, index=True)
    url: str | None           = Field(default=None, index=True)

class Document(DocumentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class DocumentPublic(DocumentBase):
    id: int

class DocumentCreate(DocumentBase):
    file: UploadFile | None = None

class DocumentUpdate(DocumentBase):
    name: str | None = None
    author: str | None = None
    title: str | None = None
    document_type: str | None = None
    file_path: str | None = None
    tags: str | None = None
    arxivId: str | None = None
    doi: str | None = None
    citation: str | None = None
    url: str | None = None
