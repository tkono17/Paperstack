import logging
from typing import Optional
from sqlmodel import select
from fastapi import HTTPException

from .base import app, SessionDep
from ..model import QueryCondition, QueryConditionPublic, QueryConditionCreate, QueryConditionUpdate
from ..model import Query, QueryPublic, QueryCreate, QueryUpdate
from ..model import QueryConditionLink

log = logging.getLogger(__name__)
          
#------------------------------------------------------------------------
# Query condition
#------------------------------------------------------------------------
@app.post('/querycondition/create', response_model=QueryConditionPublic)
def createQueryCondition(data: QueryConditionCreate, session: SessionDep):
    data_db = QueryCondition.model_validate(data)
    session.add(data_db)
    session.commit()
    session.refresh(data_db)
    return data_db

@app.get('/querycondition/', response_model=list[QueryConditionPublic])
def getQueryConditions(session: SessionDep, query_id: Optional[int] = None):
    conditions = []
    if query_id is None:
        statement = select(QueryCondition)
        conditions = session.exec(statement).all()
    else:
        statement = select(QueryCondition)
        conditions = session.exec(statement).all()
    return conditions

@app.get('/querycondition/{qc_id}', response_model=QueryConditionPublic)
def getQueryCondition(qc_id: int, session: SessionDep):
    data_db = session.get(QueryCondition, qc_id)
    if data_db is None:
        raise HTTPException(status_code=404, detail=f'Query condition {qc_id} not found')
    return data_db

@app.patch('/querycondition/update/{qc_id}', response_model=QueryConditionPublic)
def updateQueryCondition(qc_id: int, data: QueryConditionUpdate, session: SessionDep):
    data_db = session.get(QueryCondition, qc_id)
    if data_db is None:
        raise HTTPException(status_code=404, detail=f'Query condition {qc_id} not found')
    data_update = data.model_dump(exclude_unset=True)
    data_db.sqlmodel_update(data_update)
    session.add(data_db)
    session.commit()
    session.refresh(data_db)
    return data_db

@app.post('/querycondition/{qc_id}')
def deleteQueryCondition(qc_id: int, session: SessionDep):
    data_db = session.get(QueryCondition, qc_id)
    if data_db is None:
        raise HTTPException(status_code=404, detail=f'Query condition {qc_id} not found')
    session.delete(data_db)
    session.commit()
    return {'ok': True}

#------------------------------------------------------------------------
# Query
#------------------------------------------------------------------------
@app.post('/query/create', response_model=list[QueryPublic])
def createQuery(data: QueryCreate, session: SessionDep):
    data_db = Query.model_validate(data)
    session.add(data_db)
    session.commit()
    session.refresh(data_db)
    return data_db
    
@app.get('/query/', response_model=list[QueryPublic])
def getQueries(session: SessionDep, query_id: Optional[int] = None):
    queries = []
    if query_id is None:
        statement = select(Query)
        queries = session.exec(statement).all()
    else:
        statement = select(Query)
        queries = session.exec(statement).all()
    return queries

@app.get('/query/{query_id}', response_model=QueryPublic)
def getQuery(query_id: int, session: SessionDep):
    data_db = session.get(Query, query_id)
    if data_db is None:
        raise HTTPException(status_code=404, detail=f'Query condition {query_id} not found')
    return data_db

@app.patch('/query/update/{query_id}', response_model=QueryPublic)
def updateQuery(query_id: int, data: QueryUpdate, session: SessionDep):
    data_db = session.get(Query, query_id)
    if data_db is None:
        raise HTTPException(status_code=404, detail=f'Query condition {query_id} not found')
    data_update = data.model_dump(exclude_unset=True)
    data_db.sqlmodel_update(data_update)
    session.add(data_db)
    session.commit()
    session.refresh(data_db)
    return data_db

@app.post('/query/{query_id}')
def deleteQuery(query_id: int, session: SessionDep):
    data_db = session.get(Query, query_id)
    if data_db is None:
        raise HTTPException(status_code=404, detail=f'Query condition {query_id} not found')
    session.delete(data_db)
    session.commit()
    return {'ok': True}

