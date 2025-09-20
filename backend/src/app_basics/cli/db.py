import logging
import typer
from typing import Any

app = typer.Typer()
log = logging.getLogger(__name__)

@app.command('reset')
def db_reset(url: str):
    pass

@app.command('create_tables')
def db_create_tables():
    pass

@app.command('add')
def db_add(url: str, entry: str):
    pass

@app.command('read')
def db_read(url: str, id: str):
    pass

@app.command('delete')
def db_delete(url: str, id: str):
    pass
