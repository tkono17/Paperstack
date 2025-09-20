from ..utils import Settings, DbAccess, readConfig
from ...app_basics.app.stores import QueryStore, DocTypeStore

class App:
    def __init__(self):
        self.configSettings = None
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
