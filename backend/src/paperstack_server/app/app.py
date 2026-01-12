from ..db import DbAccess
from ..config import readConfig, Settings
from .stores import QueryStore, DocTypeStore

class App:
    def __init__(self):
        self.settings = None
        self.db = None
        self.queryStore = None
        self.docTypeStore = None
        #
        self.documents = []
        self.querySelected = None
        self.documentSelected = None
        
    def init(self):
        settings = Settings()
        readConfig(settings)
        self.db = DbAccess()
        self.queryStore = QueryStore()
        self.docTypeStore = DocTypeStore()
        

sApp = App()

def getApp():
    global sApp
    return sApp
