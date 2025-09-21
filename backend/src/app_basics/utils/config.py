import logging
import configparser
from typing import Any, Optional
from pathlib import Path
from dataclasses import make_dataclass, field, asdict
from ..model import ConfigSettings

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
    try:
        block = getattr(settings, section.name)
    except AttributeError as e:
        log.warning(f'Cannot find key {section.name} in settings: {e}')
        return
    for k in section.keys():
        v = section[k]
        log.info(f'item: {k} -> {v}')
        try:
            setattr(block, k, v)
        except AttributeError as e:
            log.warning(f'Cannot find key {k} in setting under {section.name}: {e}')
            continue

def makeSettings(parser):
    subObjects = {}
    fields1, values1 = [], {}
    for sn in parser.sections():
        section = parser[sn]
        fields2 = [ (key, Optional[Any], field(default=None)) for key in section.keys() ]
        values2 = { key: section[key] for key in section.keys() }
        SubCls = make_dataclass(cls_name=section.name, fields=fields2)
        fields1.append( (sn, SubCls) )
        values1[sn] = SubCls(**values2)
    Cls = make_dataclass(cls_name='SettingsDyn', fields=fields1)
    settings = Cls(**values1)
    log.debug(f'Settings created dynamincally {settings}')
    return settings

class ConfigReader:
    def __init__(self, configSettings):
        self.configSettings = configSettings

    def readConfig(self, settings=None):
        log.info(self.configSettings)
        if not validateConfigFile(self.configSettings):
            log.warning('No valid config file was found. Cannot read settings')
            return None
        fn = self.configSettings.configFileUsed
        with open(fn, 'r'):
            parser = configparser.ConfigParser()
            parser.optionxform = str
            parser.read(fn)
            log.info(parser.items())
            if settings is None:
                log.info('Make Settings dynamically')
                settings = makeSettings(parser)
            for key in parser.sections():
                section = parser[key]
                log.info(f'  Add section {key} -> {section}')
                addSection(settings, section)
        return settings

