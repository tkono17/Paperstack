import logging
import typer
from typing import Any
from ..model import Store

app = typer.Typer()

log = logging.getLogger(__name__)

@app.command('reset')
def store_reset(store_name: str):
    pass

@app.command('create')
def store_create(store_name: str):
    pass

@app.command('add')
def store_add(store_name: str, entry: Any):
    pass

@app.command('read')
def store_read(store_name: str, id: str):
    pass

@app.command('delete')
def store_delete(store_name: str, id: str):
    pass
