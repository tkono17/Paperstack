import os
import configparser
import logging
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger(__name__)

@dataclass
class Settings:
    storageDir: str | None = None
    filesDir: str | None = None
    sqliteFileName: str | None = None
    sqliteUrl: str | None = None

def sectionValue(section, key):
    x = None
    if section is not None and key in section:
        x = section[key]
    return x

    
def readConfig(settings: Settings, configFile: Path | None = None):
    settings.storageDir = os.environ['HOME']
    settings.sqliteFileName='paperstack.db'
    settings.sqliteUrl=f'sqlite:////tmp/{settings.sqliteFileName}'

    log.info(f'Read configuration from {configFile}')
    if configFile is not None and configFile.exists():
        config = configparser.ConfigParser()
        config.read(configFile)

        if 'Application' in config:
            section = config['Application']
            settings.storageDir = sectionValue(section, 'storageDir')
            filesDir = sectionValue(section, 'filesDir')
            if filesDir is None:
                settings.filesDir = Path(settings.storageDir)/'files'
                log.info(f'filesDir = {settings.filesDir}')
            else:
                settings.filesDir = filesDir
                log.info(f'filesDir2 = {settings.filesDir}')
            if not os.path.exists(settings.storageDir):
                os.mkdir(settings.storageDir)
            if not os.path.exists(settings.filesDir):
                os.mkdir(settings.filesDir)
            settings.storageType = sectionValue(section, 'storageType')
        if settings.storageType == 'sqlite' and 'Sqlite' in config:
            section = config['Sqlite']
            settings.sqliteFileName = sectionValue(section, 'fileName')
            settings.sqliteUrl = f'sqlite:///{settings.storageDir}/{settings.sqliteFileName}'
    else:
        return setting
    return setting

def defaultConfigFile():
    fp1 = Path(os.environ['HOME'])/'.paperstack.cfg'
    fp2 = Path(__file__).parent / 'paperstack.cfg'
    if fp1.exists():
        return fp1
    else:
        return fp2
