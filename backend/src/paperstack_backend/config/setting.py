import configparser
from dataclasses import dataclass
from pathlib import Path
import os

@dataclass
class Setting:
    dataDir: str | None = None
    sqliteFileName: str | None = None
    sqliteUrl: str | None = None

setting = Setting()

def readConfigValue(config, section, key):
    x = None
    if config is None:
        return x
    elif section in config:
        items = config[section]
        if key in items:
            x = items[key]
    return x

    
def readConfig(configFile: Path | None = None):
    global setting
    setting.dataDir = os.environ['HOME']
    setting.sqliteFileName='pstack.db'
    setting.sqliteUrl='sqlite:////tmp/pstack.db'
    
    if configFile is not None and configFile.exists():
        config = configparser.ConfigParser()
        config.read(configFile)
        
        setting.dataDir = readConfigValue('Application', 'dataDir')
        setting.storageType = readConfigValue('Application', 'storageType')
        if storageType == 'sqlite':
            setting.sqliteFileName = readConfigValue('Sqlite', 'fileName')
            setting.sqliteUrl = f'sqlite:///{setting.dataDir}/{setting.sqliteFileName}'
    else:
        return setting
    return setting
