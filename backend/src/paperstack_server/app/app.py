from dataclasses import dataclass, field
from typing import Optional
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
class StorageSettings:
    workDir: Optional[int] = field(init=True, default=None)
    filesDir: Optional[str] = field(init=True, default=None)
    sqliteFile: Optional[str] = field(init=True, default=None)
    sqliteUrl: Optional[str] = field(init=True, default=None)

    def __post_init__(self):
        self.sqliteUrl = 'sqlite:///'

@dataclass
class PaperstackSettings:
    configFilePath: Optional[str] = field(default=None)
    storage: StorageSettings = field(init=True, default_factory='StorageSettings')

    def __init__(self):
        self.configFilePath = None
        self.storage = StorageSettings()
        print('Paperstack init called')
        print(dir(self))

class App:
    def __init__(self):
        self.configSettings = ConfigSettings(configFileEnv='PAPERSTACK_CONFIG',
                                             cwdConfigFile='paperstack.cfg',
                                             homeConfigFile='.paperstack.cfg',
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
        print(dir(PaperstackSettings))
        settings = PaperstackSettings()
        self.settings = reader.readConfig(settings)
        print('storage: ', settings.storage)
        self.utils.init(self.settings)
        self.db = self.utils.db
        initStores(self.docTypeStore, self.queryStore)
        

sApp = App()

def getApp():
    global sApp
    return sApp
