import logging
import typer
import uvicorn
from ..api import app

log = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    log.info(f'Run the paperstack server')
    config = uvicorn.Config('paperstack_server.cli.server:app', port=3100, log_level='info')
    server = uvicorn.Server(config)
    server.run()
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    log.info(f'Paperstack server program')
    config = uvicorn.Config('paperstack_server.cli.server:app', port=3100, log_level='info')
    server = uvicorn.Server(config)
    server.run()
