import os
import logging
import configparser
import dotenv
from typing import Any, Optional
from pathlib import Path
from dataclasses import make_dataclass, field, asdict
from ..model import ConfigSettings

log = logging.getLogger(__name__)

sConfigSettings = None
sConfigFileEnv_default = 'APPBASICS_CONFIG_FILE'
sHomeConfigFile_default = 'appbasics.cfg'

def createConfigSettings(configFileEnv: Optional[str] = sConfigFileEnv_default,
                         homeConfigFile: Optional[str] = sHomeConfigFile_default,
                         systemConfigPath: Optional[str] = None):
    global sConfigSettings
    sConfigSettings = ConfigSettings(configFileEnv,
                                     homeConfigFile,
                                     systemConfigPath)
    return sConfigSettings

def getConfigSettings():
    global sConfigSettings
    if sConfigSettings is None:
        sConfigSettings = createConfigSettings()
    return sConfigSettings

def setConfigDefaults(configFileEnv: Optional[str] = None,
                      homeConfigFile: Optional[str] = None):
    global sConfigFileEnv_default
    global sHomeConfigFile_default
    if configFileEnv is not None:
        sConfigFileEnv_default = configFileEnv
    if homeConfigFile is not None:
        sHomeConfigFile_default = homeConfigFile
    pass
    
def validateConfigFile(configSettings):
    if configSettings is None:
        log.warning('ConfigSettings is None')
        return False
    return True

def sectionValue(section, key):
    x = None
    if section is not None and key in section:
        x = section[key]
    return x

def addValues(settings, section):
    for k in section.keys():
        v = section[k]
        log.info(f'item: {k} -> {v}')
        try:
            setattr(settings, k, v)
        except AttributeError as e:
            log.warning(f'Cannot find key {k} in setting under {section.name}: {e}')
            continue

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
    def __init__(self,
                 configPath: Optional[str]=None,
                 configSettings: Optional[ConfigSettings] = None):
        self.configPath = configPath
        self.configSettings = configSettings
        self.configFileUsed = None
        self.defaultSection = 'application'

        dotenv.load_dotenv('.env')
        self.selectConfigFile()

    def selectConfigFile(self):
        self.configFileUsed = None
        if self.configPath is not None and os.path.exists(self.configPath):
            self.configFileUsed = self.configPath
        elif self.configSettings is not None:
            if self.configSettings.configFileEnv is not None:
                envVar = self.configSettings.configFileEnv
                if envVar in os.environ:
                    fn = os.environ[envVar]
                    if os.path.exists(fn):
                        self.configFileUsed = fn
                        log.info(f'Configuration file selected from env. variable ({envVar}), {fn}')
            elif self.configSettings.homeConfigFile is not None:
                fn = self.configSettings.homeConfigFile
                fn = os.path.join(os.environ['HOME'], fn)
                if os.path.exists(fn):
                    self.configFileUsed = fn
                    log.info(f'Configuration file in the home directory is selected, {fn}')
            elif self.configSettings.systemConfigFile is not None:
                fn = self.configSettings.systemConfigFile
                if os.path.exists(fn):
                    self.configFileUsed = fn
                    log.info(f'System configuration file is selected, {fn}')
            else:
                log.error(f'No default method to locate the configuration file is specified')
        return self.configFileUsed
    
    def readConfig(self, settings=None):
        if self.configFileUsed is None:
            log.warning(f'No valid configuration file is found')
            return
        
        with open(self.configFileUsed, 'r'):
            parser = configparser.ConfigParser()
            parser.optionxform = str
            parser.read(self.configFileUsed)
            log.info(parser.items())
            if settings is None:
                log.info('Make Settings dynamically')
                settings = makeSettings(parser)
            for key in parser.sections():
                section = parser[key]
                log.info(f'  Add section {key} -> {section}')
                if section.name == self.defaultSection:
                    addValues(settings, section)
                else:
                    addSection(settings, section)
        return settings

