#-----------------------------------------------------------------------
# Application data model
#
# DocumentType (Base, Public, Create, Update)
# Document (Base, Public, Create, Update)
# DocumentCollection (Base, Public, Create, Update)
#-----------------------------------------------------------------------
from enum import Enum
from fastapi import UploadFile
from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Config(BaseModel):
    storageDir : str = '.'
    
#-----------------------------------------------------
# DocType
#-----------------------------------------------------
#class DocTypeBase(SQLModel):
#    name: str

#class DocType(DocTypeBase, table=True):
#    id: int = Field(index=True)

#DocTypeCreate = DocTypeBase

#class DocTypeUpdate(DocTypeBase):
#    name: str | None = None

#-----------------------------------------------------
# Document
#-----------------------------------------------------
class DocumentBase(SQLModel):
    name: str = Field(index=True)
    authors: str | None = Field(default=None, index=True)
    title: str | None = Field(default=None, index=True)
    documentType: str | None = Field(default=None, index=True)
    filePath: str | None = Field(default=None, index=True)
    tags: str = Field(default=None, index=True)
    arxivId: str | None = Field(default=None, index=True)
    doi: str | None = Field(default=None, index=True)
    reference: str | None = Field(default=None, index=True)

class Document(DocumentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class DocumentPublic(DocumentBase):
    id: int

class DocumentCreate(DocumentBase):
    file: UploadFile | None

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

#-----------------------------------------------------
# DocCollection
#-----------------------------------------------------
#class DocCollectionBase(SQLModel):
#    name: str = Field(index=True)
#    title: str | None = Field(index=True)
#    queryString: str | None = Field(index=True)
#    itemsPerPage: int | None = Field(index=True)
#class DocCollection(DocCollectionBase, table=True):
#    id: int = Field(primary_key=True)
