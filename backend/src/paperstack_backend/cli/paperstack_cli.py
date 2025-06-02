import logging
import typer
from ..db import document, docType, docCollection

logger = logging.getLogger(__name__)

app = typer.Typer()
app.add_typer(document.app, name='document')
app.add_typer(docType.app, name='docType')
app.add_typer(docCollection.app, name='docCollection')

logging.basicConfig(level=logging.INFO,
                    format='%(name)-20s %(levelname)-8s %(message)s')

if __name__ == '__main__':
    app()
    
    
    
