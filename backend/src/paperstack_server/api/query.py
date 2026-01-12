from .base import app, SessionDep
from ..model import QueryCondition, QueryConditionPublic, QueryConditionCreate, QueryConditionUpdate
from ..model import Query, QueryPublic, QueryCreate, QueryUpdate

          
#------------------------------------------------------------------------
# Query condition
#------------------------------------------------------------------------
@app.get('/querycondition/', response_model=list[QueryConditionPublic])
def createQueryCondition(data: QueryConditionCreate, session: SessionDep):
    db_data = QueryCondition.model_validate(data)
    session.add(db_data)
    session.commit()
    session.refresh(db_data)
    return db_data

#@app.get('/querycondition/', response_model=list[QueryConditionPublic])
#def getQueryConditions(condition: QueryCondition):
#    return []

#------------------------------------------------------------------------
# Query
#------------------------------------------------------------------------
@app.get('/query/', response_model=list[QueryPublic])
def createQuery(data: QueryCreate, session: SessionDep):
    db_data = Query.model_validate(data)
    session.add(db_data)
    session.commit()
    session.refresh(db_data)
    return db_data
    
#@app.get('/query/', response_model=list[QueryPublic])
#def getQueries():


