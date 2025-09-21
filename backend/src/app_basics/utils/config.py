import logging
import configparser
from typing import Any
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

def addSection(settings, section):
    block = {}
    for k in section.keys():
        v = section[k]
        log.info(f'item: {k} -> {v}')
        block[k] = v
    log.info(f'Add section {section.name}')
    settings[section.name] = block
    log.info(f'{settings}')

class ConfigReader:
    def __init__(self, configSettings):
        self.configSettings = configSettings

    def readConfig(self) -> dict[str, Any]:
        log.info(self.configSettings)
        settings = {}
        if not validateConfigFile(self.configSettings):
            log.warning('No valid config file was found. Cannot read settings')
            return None
        fn = self.configSettings.configFileUsed
        with open(fn, 'r'):
            parser = configparser.ConfigParser()
            parser.optionxform = str
            parser.read(fn)
            log.info(parser.items())
            for key in parser.sections():
                section = parser[key]
                log.info(f'  Add section {key} -> {section}')
                addSection(settings, section)
        return settings

