#!/usr/bin/env python3
import logging
import typer
import uvicorn

from ..api import app

logger = logging.getLogger(__name__)

#app = typer.Typer()
#app.add_typer(document.app, name='document')
#app.add_typer(docType.app, name='docType')
#app.add_typer(docCollection.app, name='docCollection')

logging.basicConfig(level=logging.INFO,
                    format='%(name)-20s %(levelname)-8s %(message)s')

def startApp():
    app()

def startServer():
    config = uvicorn.Config('main:startApp', port=51234, log_level='info')
    server = uvicorn.Server(config)
    await server.serve()
    
if __name__ == '__main__':
    startServer()
    
    
    
