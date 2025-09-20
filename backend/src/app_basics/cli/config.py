import logging
import typer
from typing import Optional
from ..model import ConfigSettings, Settings
from ..utils import ConfigReader

app = typer.Typer()

log = logging.getLogger(__name__)

@app.command('select')
def config_select(config_file_env: Optional[str] = None,
                  home_config_file: Optional[str] = None,
                  system_config_path: Optional[str] = None):
    csettings = ConfigSettings(configFileEnv=config_file_env,
                               homeConfigFile=home_config_file,
                               systemConfigPath=system_config_path)
    log.info(f'ConfigSettings: {csettings}')
    log.info(f'  --> Configuration file used: {csettings.configFileUsed}')

@app.command('read')
def config_read(config_path: str):
    csettings = ConfigSettings(systemConfigPath=config_path)
    if csettings.configFileUsed isNone:
        log.error(f'Configuration file does not exist {csettings.configFileUsed}')
        return
    reader = ConfigReader(csettings.configFileUsed)
    settings = Settings()
    reader.readSettings(settings)
