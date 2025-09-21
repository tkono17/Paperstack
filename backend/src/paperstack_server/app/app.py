from dataclasses import dataclass
from app_basics import getUtils, ConfigSettings, StorageSettings, ConfigReader

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
    for i, dt in enumerate(docTypes):
        docTypeStore.add(dt, i+1)
    pass

@dataclass
class PStackAppSettings:
    configFilePath: Optional[str] = None


@dataclass
class PaperstackSettings:
    application: PStackAppSettings = PStackAppSettings()
    storage: StorageSettings = StorageSettings()

class App:
    def __init__(self):
        self.configSettings = ConfigSettings(configFileEnv='PAPERSTACK_CONFIG',
                                             homeConfigFile='.paperstack.cfg'
                                             systemConfigPath='/etc/paperstack.cfg')
        self.utils = getUtils()
        self.docTypeStore = self.utils.addStore('DocType')
        self.queryStore = self.utils.addStore('Query')
        #
        self.documents = []
        self.querySelected = None
        self.documentSelected = None
        
    def init(self):
        reader = ConfigReader(self.configSettings)
        settings = PaperstackSettings()
        self.settings = reader.readConfig(settings)
        self.utils.init(self.settings)
        self.db = self.utils.db
        initStores(self.docTypeStore, self.queryStore)
        

sApp = App()

def getApp():
    global sApp
    return sApp
