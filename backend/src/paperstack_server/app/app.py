from ..db import DbAccess
from ..config import readConfig, appSetting
from .stores import QueryStore, DocTypeStore

class App:
    def __init__(self):
        self.db = None
        self.setting = appSetting
        self.queryStore = None
        self.docTypeStore = None
        #
        self.documents = []
        self.querySelected = None
        self.documentSelected = None
        
    def init(self):
        readConfig()
        self.db = DbAccess()
        
    

theApp = App()
