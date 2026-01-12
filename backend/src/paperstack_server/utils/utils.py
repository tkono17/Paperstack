from .dbAccess import DbAccess
from .settings import Settings
from .stores import QueryStore, DocTypeStore


class Utils:
    def __init__(self):
        self.settings = None
        self.db = None
        self.queryStore = None
        self.docTypeStore = None
        #
        #self.documents = []
        #self.querySelected = None
        #self.documentSelected = None
        
    def init(self):
        self.settings = Settings()
        self.settings.readConfig()
        self.db = DbAccess(self.settings.sqliteUrl)
        self.queryStore = Store()
        self.docTypeStore = Store()
        
        docTypes = [ 'Article',
                     'Eprint', 
                     'Thesis', 
                     'ThesisD',
                     'ThesisM',
                     'ThesisB',
                     'Presentation',
                     'Manual', 
                     'Specification', 
                     'Tutorial',
                     'TechnicalNote', 
                     'Datasheet',
                     'Review', 
                     'Book',]
        for i, dt in enumerate(docTypes):
            self.docTypeStore.add(dt, i+1)
        

sUtils = Utils()

def getUtils():
    global sUtils
    return sUtils
