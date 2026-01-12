#-----------------------------------------------------------------------
# Application data model: Document
#-----------------------------------------------------------------------
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from .doctype import DocType

#-----------------------------------------------------
# Document
#-----------------------------------------------------
class DocumentBase(SQLModel):
    title: str | None         = Field(default=None, index=True)
    authors: str | None       = Field(default=None, index=True)
    doctype_id: int | None = Field(default=None, foreign_key='doctype.id')
    file_path: str | None     = Field(default=None, index=True)
    tags: str | None          = Field(default=None, index=True)
    eprint: str | None        = Field(default=None, index=True)
    doi: str | None           = Field(default=None, index=True)
    reference: str | None      = Field(default=None, index=True)
    url: str | None           = Field(default=None, index=True)

    
class Document(DocumentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    doctype: Optional['DocType'] = Relationship()

class DocumentPublic(DocumentBase):
    id: int

    doctype: Optional[DocType] = Field(default=None)

class DocumentCreate(DocumentBase):
    #file: UploadFile | None = None
    doctype: Optional[DocType] = Field(default=None)
    pass

class DocumentUpdate(DocumentBase):
    title: str | None = None
    authors: str | None = None
    doctype_id: str | None = None
    file_path: str | None = None
    tags: str | None = None
    eprint: str | None = None
    doi: str | None = None
    reference: str | None = None
    url: str | None = None

    doctype: Optional[DocType] = Field(default=None)

