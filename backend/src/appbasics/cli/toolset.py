import logging
import typer
from .config import app as config_app
from .db import app as db_app
from .store import app as store_app

app = typer.Typer()

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    app.add_typer(config_app, name='config')
    app.add_typer(db_app, name='db')
    app.add_typer(store_app, name='store')
    app()
    
if __name__ == '__main__':
    main()
