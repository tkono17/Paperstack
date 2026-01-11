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

class DocTypeBase(SQLModel):
    name: Optional[str] = Field(default=None, index=True)

class DocType(DocTypeBase, table=True):
    id: int = Field(default=None, primary_key=True)

class DocTypePublic(DocTypeBase):
    id: int
    
class DocTypeCreate(DocTypeBase):
    pass

class DocTypeUpdate(DocTypeBase):
    name: str | None = None

