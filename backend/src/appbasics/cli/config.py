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
def config_check(config_path: str):
    csettings = createConfigSettings(systemConfigPath=config_path)
    if csettings.configFileUsed is None:
        log.error(f'Configuration file does not exist {csettings.configFileUsed}')
        return
    reader = ConfigReader(csettings)
    settings = reader.readConfig()
    log.info(f'Settings: \n{json.dumps(asdict(settings), indent=2)}')
