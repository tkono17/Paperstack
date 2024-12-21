import sqlite3
import .models import DocumentType, Document, DocumentCollection

# DocumentType
def insertDocumentType(db, docType):
    x = db.query(DocumenType).filter(DocumentTYpe.name == docType.name).first()
    if x:
        return -1
    db.add(docType)
    db.commit()
    db.refresh(docType)
    return docType

def getDocumentType(db, docType):
    x = db.query(DocumentType).filter(DocumentType.id == docType.id).first()
    return x

def updateDocumentType(db, docType):
    pass

def deleteDocumentType(db, docType):
    x = db.query(DocumentType).filter(DocumentType.id == docType.id).first()
    if x is None:
        return -1
    db.delete(x)
    db.commit()
    return 0

# Document
def insertDocument(db, document):
    pass

def getDocument(db, document):
    x = db.query(Document).filter(Document.id == document.id).first()
    return x

def updateDocument(db, document):
    pass

def deleteDocument(db, document):
    x = db.query(Document).filter(Document.id == document.id).first()
    if x is None:
        return -1
    db.delete(x)
    db.commit()
    return 0

# DocumentCollection
def insertDocumentCollection(db, docCollection):
    pass

def getDocumentCollection(db, docCollection):
    x = db.query(DocumentCollection).filter(DocumentCollection.id == docCollection.id).first()
    return x

def updateDocumentCollection(db, docCollection):
    pass

def deleteDocumentCollection(db, docCollection):
    x = db.query(DocumentCollection).filter(DocumentCollection.id == docCollection.id).first()
    if x is None:
        return -1
    db.delete(x)
    db.commit()
    return 0
