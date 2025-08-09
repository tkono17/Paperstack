import fastapi
from sqlmodel import Session, select
from typing import Annotated, List

from . import db
#from .models import DocType, DocTypePublic, DocTypeCreate, DocTypeUpdate
from .models import Document, DocumentPublic, DocumentCreate, DocumentUpdate
#from .models import DocCollection, DocCollectionPublic, DocCollectionCreate, DocCollectionUpdate

app = fastapi.FastAPI()

SessionDep = Annotated[Session, fastapi.Depends(db.get_session)]

documentList: dict[int, DocumentPublic] = {}

@app.get('/')
def root():
    return {'message': 'Hello World'}
    
@app.post('/documents/', response_model=DocumentPublic)
def create_document(document: DocumentCreate, session: SessionDep):
    engine = db.connectDatabase('sqlite:///../../../pstack.db')
    #if doc_name == '':
    #    raise fastapi.HTTPException(status_code=400, detail='Document name cannot be empty')
    doc_ids = {item.name: item.id if item.id is not None else 0 for item in documentList.values()}

    doc_id = max(documentList.keys()) + 1 if documentList else 0
    data = Document.model_validate(document)

    session.add(data)
    session.commit()
    session.refresh(data)

    return data

@app.get('/documents/', response_model=List[DocumentPublic])
def read_documents(session: SessionDep, 
                   offset: int = 0, 
                   limit: Annotated[int, fastapi.Query(le=100)] = 100):
    docs = session.exec(select(Document).offset(offset).limit(limit)).all()
    return docs

if __name__ == '__main__':
    typer.run(app)
