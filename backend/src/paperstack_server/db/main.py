import typer
import pathlib
import logging
from ..config import readConfig, setting, defaultConfigFile
from .dbAccess import DbAccess

log = logging.getLogger(__name__)
app = typer.Typer()

@app.command('createTables')
def createTables(config_file: pathlib.Path | None = None):
    if config_file is None:
        config_file = defaultConfigFile()
    log.info(f'Read configuration from {config_file}')
    readConfig(config_file)
    log.info(f'Setting = {setting}')
    db = DbAccess.get(setting.sqliteUrl)
    db.createTables()
