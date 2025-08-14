import typer
import pathlib
import logging
from .app import getApp

log = logging.getLogger(__name__)
app = typer.Typer()

@app.command('createTables')
def createTables(config_file: pathlib.Path | None = None):
    if config_file is None:
        config_file = defaultConfigFile()
    log.info(f'Read configuration from {config_file}')
    sApp = getApp()
    log.info(f'Setting = {sApp.settings}')
    sApp.db.createTables()
