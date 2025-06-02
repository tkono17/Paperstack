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
    name: str = Field(index=True)
    authors: str | None = Field(default=None, index=True)
    title: str | None = Field(default=None, index=True)
    documentType: str | None = Field(default=None, index=True)
    filePath: str | None = Field(default=None, index=True)
    tags: str | None = Field(default=None, index=True)
    eprint: str | None = Field(default=None, index=True)
    doi: str | None = Field(default=None, index=True)
    reference: str | None = Field(default=None, index=True)

class DocumentDb(DocumentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class DocumentPublic(DocumentBase):
    id: int

class DocumentCreate(DocumentBase):
    file: UploadFile | None = None

class DocumentUpdate(DocumentBase):
    name: str | None = None
    author: str | None = None
    title: str | None = None
    documentType: str | None = None
    filePath: str | None = None
    tags: str | None = None
    arxivId: str | None = None
    doi: str | None = None
    reference: str | None = None
