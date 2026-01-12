import logging
import typer
from typing import List, Optional
from pathlib import Path
import shutil

from ..app import getApp
from ..model import QueryConditionPublic, QueryConditionCreate, QueryConditionUpdate
from ..model import QueryPublic, QueryCreate, QueryUpdate
from .. import api

query_app = typer.Typer()
log = logging.getLogger(__name__)

#------------------------------------------------------------------------
# Query condition
#------------------------------------------------------------------------
def createQueryCondition(name: str, operator: str, value: str):
    data = QueryConditionCreate(fieldName=name, operator=operator, fieldValue=value)
    app = getApp()
    session = app.db.getSession()
    return api.createQueryCondition(data, next(session))

def decodeCondition(condition):
    oplist = ['>=', '<=', '==', '!=', '>', '<', 'CONTAINS' ]
    words = ()
    for op in oplist:
        i = condition.find(op)
        if i > 0:
            name = condition[:i].strip()
            value = condition[i+len(op):].strip()
            words = (name, op, value)
    return words
    
#------------------------------------------------------------------------
# Query
#------------------------------------------------------------------------
@query_app.command('create')
def createQuery(name: str,
                logic: str='AND',
                conditions: List[str]=[]):
    if len(conditions)==0:
        log.warning('Query has no conditions')
        pass
    log.info(f'Query create:')
    log.info(f'  name: {name}')
    log.info(f'  logic: {logic}')
    log.info(f'  conditions: {conditions}')
    conds = []
    for condition in conditions:
        words = decodeCondition(condition)
        if len(words) == 3:
            fname, op, fvalue = words
            #dbc = QueryConditionCreate(fieldName=fname, operator=op, fieldValue=fvalue)
            dbc = createQueryCondition(fname, op, fvalue)
            conds.append(dbc)
    data = QueryCreate(name=name, logic=logic, conditions=conds)
    log.info(f'conds = {conds}')
    app = getApp()
    session = next(app.db.getSession())
    return api.createQuery(data, session)

