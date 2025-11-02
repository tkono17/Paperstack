import logging
import typer
from typing import Optional
import json
from dataclasses import asdict
from ..model import ConfigSettings, Settings
from ..utils import ConfigReader

app = typer.Typer()

log = logging.getLogger(__name__)

@app.command('check')
def config_check(config_path: str):
    csettings = createConfigSettings(systemConfigPath=config_path)
    if csettings.configFileUsed is None:
        log.error(f'Configuration file does not exist {csettings.configFileUsed}')
        return
    reader = ConfigReader(csettings)
    settings = reader.readConfig()
    log.info(f'Settings: \n{json.dumps(asdict(settings), indent=2)}')
    
@app.command('save')
def config_save(config_file_env: Optional[str] = None,
                system_config_path: Optional[str] = None):
    csettings = ConfigSettings(configFileEnv=config_file_env, 
                               systemConfigPath=system_config_path)
    log.info(f'ConfigSettings: {csettings}')
    log.info(f'  --> Configuration file used: {csettings.configFileUsed}')

