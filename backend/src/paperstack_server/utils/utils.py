from .dbAccess import DbAccess
from .settings import readConfig, Settings
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
        settings = Settings()
        readConfig(settings)
        self.db = DbAccess()
        self.queryStore = QueryStore()
        self.docTypeStore = DocTypeStore()
        

sUtils = Utils()

def getUtils():
    global sUtils
    return sUtils
