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
        ok = False
        if self.configFileEnv is None and \
            self.homeConfigFile is None and \
            self.systemConfigPath is None:
            log.warning(f'Nothing is specified in ConfigSettings')
            return None
        
        if self.configFileEnv is not None:
            if self.configFileEnv in os.environ:
                fn = os.environ[self.configFileEnv]
            if fn is not None and os.path.exists(fn):
                ok = True
            else:
                fn = None
        if not ok and self.homeConfigFile is not None:
            if 'HOME' in os.environ:
                fn = os.path.join(os.environ['HOME'], self.homeConfigFile)
            if os.path.exists(fn):
                ok = True
            else:
                fn = None
        if not ok and self.systemConfigPath:
            fn = self.systemConfigPath
            if os.path.exists(fn):
                ok = True
            else:
                fn = None
        self.configFileUsed = fn
    
@dataclass
class StorageSettings:
    storageDir: str
    filesDir: str
    sqliteFileName: str
    sqliteUrl: str

@dataclass
class Settings:
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
