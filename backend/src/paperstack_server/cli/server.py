import logging
import typer
import uvicorn
from ..api import app as webapp

log = logging.getLogger(__name__)

server_app = typer.Typer()

def serverMain():
    webapp()

def stringToLogLevel(sloglevel: str):
    level = logging.INFO
    match sloglevel:
        case 'DEBUG': level = logging.DEBUG
        case 'INFO': level = logging.INFO
        case 'WARNING': level = logging.WARNING
        case 'ERROR': level = logging.ERROR
    return level
        
@server_app.command()
def startServer(host: str = 'localhost',
                port: int = 7611,
                log_level: str = 'INFO'):
    logging.basicConfig(level=stringToLogLevel(log_level))
    
    config = uvicorn.Config('paperstack_server.cli.server:webapp',
                            host=host, port=port,
                            log_level='info')
    server = uvicorn.Server(config)
    server.run()

def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    log.info('Start server program')
    server_app()
    
if __name__ == '__main__':
    main()
