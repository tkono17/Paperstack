from typing import Optional
from appbasics import getUtils, ConfigSettings, StorageSettings, ConfigReader
import logging
from ..model import PaperstackSettings

log = logging.getLogger(__name__)

class App:
    def __init__(self):
        self.configSettings = ConfigSettings(configFileEnv='PAPERSTACK_CONFIG',
                                             homeConfigFile='.paperstack.cfg')
        self.utils = getUtils()
        #self.docTypeStore = self.utils.addStore('DocType')
        #self.queryStore = self.utils.addStore('Query')
        #
        self.documents = []
        self.querySelected = None
        self.documentSelected = None
        log.info(f'Application created')
        
    def init(self, configPath=None):
        logging.basicConfig(level=logging.INFO,
                    format='%(name)-20s %(levelname)-8s %(message)s')
        reader = ConfigReader(configPath=configPath,
                              configSettings=self.configSettings)
        self.settings = reader.readConfig(PaperstackSettings())
        log.debug(f'Settings: {self.settings}')
        self.utils.init(self.settings)
        self.db = self.utils.db
        log.info(self.db)
        

sApp = App()

def getApp():
    global sApp
    return sApp

