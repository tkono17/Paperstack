import logging
import typer
import uvicorn
from ..api import app as webapp

log = logging.getLogger(__name__)


def serverMain():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    log.info('Start server program')
    webapp()

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    log.info('Start server maanger')
    config = uvicorn.Config('paperstack_server.cli.server:serverMain', port=3100, log_level='info')
    server = uvicorn.Server(config)
    server.run()

    
if __name__ == '__main__':
    main()

