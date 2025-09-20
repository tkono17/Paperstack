import logging
import typer
from . import config
from . import db
from . import store

app = typer.Typer()

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    app.add_typer(config.app, name='config')
    app.add_typer(db.app, name='db')
    app.add_typer(store.app, name='store')
    app()
    
if __name__ == '__main__':
    main()
