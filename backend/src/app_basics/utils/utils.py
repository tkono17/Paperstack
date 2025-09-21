from ..model import Store
from .dbAccess import DbAccess


class Utils:
    def __init__(self):
        self.settings = None
        self.db = None
        self.stores = {}

    def init(self, settings=None):
        if settings is not None:
            self.settings = settings
        self.db = DbAccess(settings.storage.sqliteUrl)
        
    def addStore(self, sname):
        store = None
        if sname not in self.stores.keys():
            store = Store()
            self.stores[sname] = store
        return store

sUtils = Utils()

def getUtils():
    global sUtils
    return sUtils
