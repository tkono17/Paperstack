import logging
import typer
from typing import Optional
import json
from dataclasses import asdict
from ..model import ConfigSettings
from ..utils import ConfigReader, createConfigSettings, getConfigSettings

app = typer.Typer()

log = logging.getLogger(__name__)

@app.command('check')
def config_check(use_config_path: Optional[bool] = None,
                 config_file_env: Optional[str] = None,
                 home_config_file: Optional[str] = None,
                 system_config_file: Optional[str] = None,
                 config_path: Optional[str] = None):
    csettings = ConfigSettings(useConfigPath=use_config_path,
                               configFileEnv=config_file_env,
                               homeConfigFile=home_config_file,
                               systemConfigPath=system_config_file)
    if csettings.configFileUsed is None:
        log.error(f'Configuration file does not exist {csettings.configFileUsed}')
        return
    reader = ConfigReader(csettings)
    settings = reader.readConfig()
    log.info(f'Settings: \n{json.dumps(asdict(settings), indent=2)}')
