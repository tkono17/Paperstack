import logging
import typer
import uvicorn
from ..api import app as webapp

log = logging.getLogger(__name__)

app = typer.Typer()

def serverMain():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    log.info('Start server program')
    webapp()

@app.command()
def startServer(port=61234):
    config = uvicorn.Config('paperstack_server.cli.server:serverMain', port=port, log_level='info')
    server = uvicorn.Server(config)
    server.run()
    
def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    log.info('Start server program')
    app()
    
if __name__ == '__main__':
    main()

