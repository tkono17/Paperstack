import logging
import configparser
from pathlib import Path
from ..model import ConfigSettings, Settings

log = logging.getLogger(__name__)

def sectionValue(section, key):
    x = None
    if section is not None and key in section:
        x = section[key]
    return x

def validateConfigFile(configSettings):
    fn = None
    if configSettings is None:
        log.warning('ConfigSettings is None')
        fn = configSettings.usedConfigFile()
    if fn is None:
        log.warning(f'Configuration file is None')
        fn = configSettings.usedConfigFile()
        return None
    if not Path(fn).exists():
        log.warning(f'Configuration file {fn} does not exist')
        return None
    return fn

class ConfigReader:
    def __init__(self, configSettings):
        self.configSettings = configSettings


    def readSettings(self, settings):
        fn = validateConfigFile(self.configSettings)
        if fn is None:
            log.warning('No valid config file was found. Cannot read settings')
            return None
        with open(fn, 'r'):
            parser = configparser.ConfigParser()
            parser.read(fn)
            log.info(f'{parser.section.keys()}')
            log.info(f'{dir(settings)}')
            pass
        pass

