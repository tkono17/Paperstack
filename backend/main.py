from fastapi import FastAPI, HTTPException
from models import DocumentType, Document, DocumentCollection

app = FastAPI()

documentList: dict[int, Document] = {}

@app.get('/')
def root():
    return {'message': 'Hello World'}
    
@app.post('/documents/{doc_name}')
def addDocument(doc_name: str) -> dict[str, Document]:
    #if doc_name == '':
    #    raise HTTPException(status_code=400, detail='Document name cannot be empty')
    doc_ids = {item.name: item.id if item.id is not None else 0 for item in documentList.values()}
    if doc_name in doc_ids.keys():
        doc_id = doc_ids[doc_name]
    else:
        doc_id = max(documentList.keys()) + 1 if documentList else 0
        documentList[doc_id] = Document(id=doc_id, name=doc_name)
    
    return {'item': documentList[doc_id]}
