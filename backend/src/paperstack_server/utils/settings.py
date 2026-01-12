import os
import configparser
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

log = logging.getLogger(__name__)

@dataclass
class Settings:
    configFileEnv: Optional[str] = None
    homeConfigFile: Optional[str] = None
    defaultConfigFile: Optional[str] = None
    storageDir: str | None = None
    filesDir: str | None = None
    sqliteFileName: str | None = None
    sqliteUrl: str | None = None

    @classmethod
    def init(cls,
             configFileEnv: str,
             homeConfigFile: str,
             defaultConfigFile: str):
        Settings.configFileEnv = configFileEnv
        Settings.homeConfigFile = homeConfigFile
        Settings.defaultConfigFile = defaultConfigFile
        
    def readConfig(self, configFile: Path | None = None):
        self.storageDir = os.environ['HOME']
        self.sqliteFileName='paperstack.db'
        self.sqliteUrl=f'sqlite:////tmp/{self.sqliteFileName}'

        if configFile is None:
            if Settings.configFileEnv is not None and\
               Settings.configFileEnv in os.environ and \
               Path(os.environ[Settings.configFileEnv]).exists():
                configFile = os.environ[Settings.configFileEnv]
            elif Settings.homeConfigFile is not None and\
                 Path(Settings.homeConfigFile).exists():
                configFile = Settings.homeConfigFile
            elif Settings.homeConfigFile is not None and\
                 Path(Settings.homeConfigFile).exists():
                configFile = Settings.defaultConfigFile
        log.info(f'Read configuration from {configFile}')
        
        if configFile is not None and configFile.exists():
            config = configparser.ConfigParser()
            config.read(configFile)
            
            if 'Application' in config:
                section = config['Application']
                self.storageDir = sectionValue(section, 'storageDir')
                filesDir = sectionValue(section, 'filesDir')
                if filesDir is None:
                    self.filesDir = Path(self.storageDir)/'files'
                    log.info(f'filesDir = {self.filesDir}')
                else:
                    self.filesDir = filesDir
                log.info(f'filesDir2 = {self.filesDir}')
                if not os.path.exists(self.storageDir):
                    os.mkdir(self.storageDir)
                if not os.path.exists(self.filesDir):
                    os.mkdir(self.filesDir)
                self.storageType = sectionValue(section, 'storageType')
            if self.storageType == 'sqlite' and 'Sqlite' in config:
                section = config['Sqlite']
                self.sqliteFileName = sectionValue(section, 'fileName')
                self.sqliteUrl = f'sqlite:///{self.storageDir}/{self.sqliteFileName}'
        pass
    pass

def sectionValue(section, key):
    x = None
    if section is not None and key in section:
        x = section[key]
    return x

    

def defaultConfigFile():
    fp1 = Path(os.environ['HOME'])/'.paperstack.cfg'
    fp2 = Path(__file__).parent / 'paperstack.cfg'
    if fp1.exists():
        return fp1
    else:
        return fp2
