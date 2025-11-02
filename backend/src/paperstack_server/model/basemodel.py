from dataclasses import dataclass
from typing import Optional, List

@dataclass
class DocType:
    name: str

@dataclass
class Document:
    name: str
    authors: Optional[str] = None
    title: Optional[str] = None
    document_type: Optional[DocType] = None
    file_path: Optional[str] = None
    tags: Optional[str] = None
    eprint: Optional[str] = None
    doi: Optional[str] = None
    citation: Optional[str] = None
    url: Optional[str] = None

@dataclass
class SimpleQuery:
    name: str
    op: Optional[str] = None
    fieldName: Optional[str] = None
    value: str | int | float | None = None

@dataclass
class CompositeQuery:
    name: str
    logic: Optional[str] = None
    subQueryNames: List[str] | None = None

