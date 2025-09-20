import logging
import configparser
from pathlib import Path
from ..model import ConfigSettings, Settings

log = logging.getLogger(__name__)

def validateConfigFile(configSettings):
    if configSettings is None:
        log.warning('ConfigSettings is None')
        return False
    if configSettings.configFileUsed is None:
        log.warning(f'Configuration file is None')
        return False
    if not Path(configSettings.configFileUsed).exists():
        log.warning(f'Configuration file {configSettings.configFileUsed} does not exist')
        return False
    return True

def sectionValue(section, key):
    x = None
    if section is not None and key in section:
        x = section[key]
    return x

def addSection(settings, sectionName, section):
    block = {}
    block.update(section)
    setattr(settings, sectionName, block)
    log.info(f'{dir(settings)}')

class ConfigReader:
    def __init__(self, configSettings):
        self.configSettings = configSettings

    def readSettings(self, settings):
        log.info(self.configSettings)
        if not validateConfigFile(self.configSettings):
            log.warning('No valid config file was found. Cannot read settings')
            return None
        fn = self.configSettings.configFileUsed
        with open(fn, 'r'):
            parser = configparser.ConfigParser()
            parser.read(fn)
            log.info(parser.items())
            for key in parser.sections():
                section = parser[key]
                log.info(f'{key} -> {section}')
                addSection(settings, key, section)
            pass
        pass

