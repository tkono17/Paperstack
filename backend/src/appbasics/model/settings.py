import os
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
