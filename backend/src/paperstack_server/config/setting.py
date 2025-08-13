import configparser
import logging
from dataclasses import dataclass
from pathlib import Path
import os

log = logging.getLogger(__name__)

@dataclass
class Setting:
    storageDir: str | None = None
    filesDir: str | None = None
    sqliteFileName: str | None = None
    sqliteUrl: str | None = None

appSetting = Setting()

def sectionValue(section, key):
    x = None
    if section is not None and key in section:
        x = section[key]
    return x

    
def readConfig(configFile: Path | None = None):
    global setting
    setting.storageDir = os.environ['HOME']
    setting.sqliteFileName='paperstack.db'
    setting.sqliteUrl=f'sqlite:////tmp/{setting.sqliteFileName}'

    log.info(f'Read configuration from {configFile}')
    if configFile is not None and configFile.exists():
        config = configparser.ConfigParser()
        config.read(configFile)

        if 'Application' in config:
            section = config['Application']
            setting.storageDir = sectionValue(section, 'storageDir')
            filesDir = sectionValue(section, 'filesDir')
            if filesDir is None:
                setting.filesDir = Path(setting.storageDir)/'files'
                log.info(f'filesDir = {setting.filesDir}')
            else:
                setting.filesDir = filesDir
                log.info(f'filesDir2 = {setting.filesDir}')
            if not os.path.exists(setting.storageDir):
                os.mkdir(setting.storageDir)
            if not os.path.exists(setting.filesDir):
                os.mkdir(setting.filesDir)
            setting.storageType = sectionValue(section, 'storageType')
        if setting.storageType == 'sqlite' and 'Sqlite' in config:
            section = config['Sqlite']
            setting.sqliteFileName = sectionValue(section, 'fileName')
            setting.sqliteUrl = f'sqlite:///{setting.storageDir}/{setting.sqliteFileName}'
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
