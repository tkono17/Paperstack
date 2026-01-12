from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

#------------------------------------------------------------------------
# Query condition
#------------------------------------------------------------------------
class QueryConditionBase(SQLModel):
    fieldName: Optional[str] = Field(default=None, index=True)
    operator: Optional[str] = Field(default=None)
    fieldValue: Optional[str] = Field(default=None, index=True)

class QueryCondition(QueryConditionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class QueryConditionPublic(QueryConditionBase):
    id: int

class QueryConditionCreate(QueryConditionBase):
    pass

class QueryConditionUpdate(QueryConditionBase):
    fieldName: Optional[str] = None
    operator: Optional[str] = None
    fieldValue: Optional[str] = None

#------------------------------------------------------------------------
# Query-condition link
#------------------------------------------------------------------------
class QueryConditionLink(SQLModel, table=True):
    query_id: Optional[int] = Field(default=None, foreign_key='query.id', primary_key=True)
    condition_id: Optional[int] = Field(default=None, foreign_key='querycondition.id', primary_key=True)

#------------------------------------------------------------------------
# Query
#------------------------------------------------------------------------
class QueryBase(SQLModel):
    name: Optional[str] = Field(default=None, index=True)
    logic: Optional[str] = Field(default='AND', index=True)

class Query(QueryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    conditions: List[QueryCondition] | None = Relationship(link_model=QueryConditionLink)

class QueryPublic(QueryBase):
    id: int
    conditions: List[QueryCondition] | None = Field(default=None)

class QueryCreate(QueryBase):
    conditions: List[QueryCondition] | None = Field(default=None)

class QueryUpdate(QueryBase):
    name: Optional[str] = None
    logic: Optional[str] = 'AND'
    conditions: Optional[List[QueryCondition]] = Field(default=None)
    
