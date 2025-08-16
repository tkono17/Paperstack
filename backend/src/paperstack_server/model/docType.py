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

class DocTypeBase(BaseModel):
    name: str | None = None #Field(default=None, index=True)

DocType = DocTypeBase
#class DocType(DocTypeBase, table=True):
#    id: int = Field(default=None, primary_key=True)

DocTypeCreate = DocTypeBase

class DocTypePublic(DocTypeBase):
    id: int

class DocTypeUpdate(DocTypeBase):
    name: str | None = None

