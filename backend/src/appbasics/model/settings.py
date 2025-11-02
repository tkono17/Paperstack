import os
import configparser
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

log = logging.getLogger(__name__)

@dataclass
class ConfigSettings:
    configFileEnv: Optional[str] = None
    homeConfigFile: Optional[str] = None
    systemConfigPath: Optional[str] = None
    configFileUsed: Optional[str] = None

    def __post_init__(self):
        fn = None
        doCheck = True
        
        def isOk(self):
            return ok
        
        if self.configFileEnv is None and \
            self.homeConfigFile is None and \
            self.systemConfigPath is None:
            log.warning(f'Nothing is specified in ConfigSettings')
            return None
        
        if doCheck and self.configFileEnv is not None:
            if self.configFileEnv is not None:
                if self.configFileEnv in os.environ:
                    fn = os.environ[self.configFileEnv]
                if fn is not None and os.path.exists(fn):
                    doCheck = False
                else:
                    fn = None
        
        if doCheck and self.homeConfigFile is not None:
            if 'HOME' in os.environ:
                fn = os.path.join(os.environ['HOME'], self.homeConfigFile)
            if os.path.exists(fn):
                doCheck = False
            else:
                fn = None

        if doCheck and self.systemConfigPath:
            fn = self.systemConfigPath
            if os.path.exists(fn):
                doCheck = False
            else:
                fn = None
        self.configFileUsed = fn
    

@dataclass
class StorageSettings:
    storageDir: Optional[str] = None
    filesDir: Optional[str] = None
    sqliteUrl: Optional[str] = None

    def __post_init__(self):
        if os.path.exists(self.storageDir):
            self.filesDir = os.path.join(self.storageDir, 'files')
        pass

@dataclass
class BasicSettings:
    configFilePath: Optional[str] = None
    storage: Optional[StorageSettings] = None
    pass
    

def defaultConfigFile():
    fp1 = Path(os.environ['HOME'])/'.paperstack.cfg'
    fp2 = Path(__file__).parent / 'paperstack.cfg'
    if fp1.exists():
        return fp1
    else:
        return fp2
