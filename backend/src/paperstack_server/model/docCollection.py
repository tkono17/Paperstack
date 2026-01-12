#-----------------------------------------------------------------------
# Application data model
#
# DocCollection (Base, Db, Public, Create, Update)
#-----------------------------------------------------------------------
from enum import Enum
from fastapi import UploadFile
from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class DocCollectionBase(SQLModel):
    name: str = Field(index=True)
    title: str | None = Field(index=True)
    queryId: str | None = Field(index=True)
    itemsPerPage: int | None = Field(index=True)

class DocCollectionDb(DocCollectionBase, table=True):
    id: int = Field(default=None, primary_key=True)

class DocCollectionPublic(DocCollectionBase):
    id: int

class DocCollectionCreate(DocCollectionBase):
    pass

class DocCollectionUpdate(DocCollectionBase):
    id: int

