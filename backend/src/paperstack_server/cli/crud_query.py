import logging
import typer
from typing import List, Optional
from pathlib import Path
import shutil

from ..app import getApp
from ..model import QueryCondition, QueryConditionPublic, QueryConditionCreate, QueryConditionUpdate
from ..model import Query, QueryPublic, QueryCreate, QueryUpdate
from .. import api

query_app = typer.Typer()
log = logging.getLogger(__name__)

#------------------------------------------------------------------------
# Query condition
#------------------------------------------------------------------------
@query_app.command('create')
def createQueryCondition(name: str, operator: str, value: str):
    data = QueryConditionCreate(name=name, operator=operator, value=value)
    app = getApp()
    session = app.db.getSession()
    return api.createQuery(data, next(session))


#------------------------------------------------------------------------
# Query
#------------------------------------------------------------------------
@query_app.command('create')
def createQuery(name: str, logic: str, conditions=List[QueryCondition]):
    data = QueryCreate(name=name, logic=logic, conditions=conditions)
    app = getApp()
    session = next(app.db.getSession())
    return api.createQuery(data, session)


