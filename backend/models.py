from enum import Enum
from typing import Optional
from pydantic import BaseModel

class DocumentType(Enum):
    id: int
    name: str

class Document(BaseModel):
    id: int
    name: str
    #author: str
    #title: str
    #documentType: str
    #tags: list[str]
    #arxivId: Optional[str]
    #doi: Optional[str]
    #reference: Optional[str]

class DocumentCollection(BaseModel):
    id: int
    name: str
    title: str
    queryString: Optional[str]
    itemsPerPage: int
    