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
    defaultConfigFile: Optional[str] = None

    def configFileUsed() -> Optional[str]:
        fn = None
        return fn
    
@dataclass
class StorageSettings:
    storageDir: str
    filesDir: str
    sqliteFileName: str
    sqliteUrl: str

@dataclass
class Settings:
    config: ConfigSettings
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
