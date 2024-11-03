from enum import Enum
from typing import Optional
from pydantic import BaseModel

class DocumentType(Enum):
    id: int
    name: str

class Document(BaseModel):
    id: int
    name: str
    author: str
    title: str
    documentType: str
    tags: list[str] = None
    arxivId: Optional[str] = None
    doi: Optional[str] = None
    reference: Optional[str] = None

class DocumentCollection(BaseModel):
    id: int
    name: str
    title: str
    queryString: Optional[str]
    itemsPerPage: int
    