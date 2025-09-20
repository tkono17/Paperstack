import logging
import typer
import uvicorn
from .app import getApp

app = typer.Typer()

log = logging.getLogger(__name__)

@app.command()
def init_db():
    log.info('Initialize database')
    sApp = getApp()
    #sApp.db.createTables()
    pass

@app.command()
def reset_db():
    log.info('Reset database')
    init_db()
    pass

@app.command()
def start_server():
    log.info(f'Run the paperstack server')
    config = uvicorn.Config('paperstack_server.cli.server:serverMain', port=3100, log_level='info')
    server = uvicorn.Server(config)
    server.run()

def serverMain():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    log.info('Start server program')
    start_server()

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    log.info('Start server maanger')
    app()
    
if __name__ == '__main__':
    main()

