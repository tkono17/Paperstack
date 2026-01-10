from typing import Optional
from appbasics import getUtils, ConfigSettings, StorageSettings, ConfigReader
import logging
from ..model import PaperstackSettings

log = logging.getLogger(__name__)

def initStores(docTypeStore, queryStore):
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
    log.info(f'Initialization of docType stores')
    for i, dt in enumerate(docTypes):
        docTypeStore.add(dt, i+1)
    pass

class App:
    def __init__(self):
        self.configSettings = ConfigSettings(configFileEnv='PAPERSTACK_CONFIG',
                                             homeConfigFile='.paperstack.cfg')
        self.utils = getUtils()
        self.docTypeStore = self.utils.addStore('DocType')
        self.queryStore = self.utils.addStore('Query')
        #
        self.documents = []
        self.querySelected = None
        self.documentSelected = None
        log.info(f'Application created')
        
    def init(self, configPath=None):
        reader = ConfigReader(configPath=configPath,
                              configSettings=self.configSettings)
        self.settings = reader.readConfig(PaperstackSettings())
        print('storage: ', self.settings.storage)
        log.info(f'Settings: {self.settings}')
        self.utils.init(self.settings)
        self.db = self.utils.db
        log.info(self.db)
        initStores(self.docTypeStore, self.queryStore)
        

sApp = App()

def getApp():
    global sApp
    return sApp
