from ..model import QOp, QL, QueryCondition, SimpleQuery, CompositeQuery, QCgen
from ..utils import Store
from .base import app, SessionDep

store = Store()
store.add('Article', 1, QCgen.condition('dt_Article', QOp.EQ, 'docType', 'Article'))
store.add('Eprint', 2, QCgen.condition('dt_Eprint', QOp.EQ, 'docType', 'Eprint'))
          
@app.get('/query/', response_model=list[SimpleQuery])
def getSimpleQueries():
    return [ x for x in store.idToX.values() ]

