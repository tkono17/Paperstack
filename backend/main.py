from fastapi import FastAPI, HTTPException
from models import DocumentType, Document, DocumentCollection

app = FastAPI()

documentList: dict[int, Document] = {}

@app.get('/')
def root():
    return {'message': 'Hello World'}
    
@app.post('/documents/{doc_name}')
def addDocument(doc_name: str, dataIn: Document) -> dict[str, Document]:
    #if doc_name == '':
    #    raise HTTPException(status_code=400, detail='Document name cannot be empty')
    doc_ids = {item.name: item.id if item.id is not None else 0 for item in documentList.values()}
    doc = None
    data = {}
    if doc_name in doc_ids.keys():
        doc_id = doc_ids[doc_name]
        doc = documentList[doc_id]
    else:
        # Properties in the pass parameter
        doc_id = max(documentList.keys()) + 1 if documentList else 0
    # Properties in the request body
    data['author'] = dataIn.author
    data['title'] = dataIn.title
    data['documentType'] = dataIn.documentType
    data['tags'] = dataIn.tags
    data['doi'] = dataIn.doi
    data['arxivId'] = dataIn.arxivId
    data['reference'] = dataIn.reference
    
    doc = Document(id=doc_id, name=doc_name, **data)
    documentList[doc_id] = doc
    return {'item': documentList[doc_id]}
