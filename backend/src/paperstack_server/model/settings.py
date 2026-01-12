# Paperstack settings
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class ApplicationSettings:
    name: str = ''
    version: str = ''

@dataclass
class StorageSettings:
    topDir: Optional[str] = None
    filesDir: Optional[str] = None
    sqliteUrl: Optional[str] = None
    
@dataclass
class PaperstackSettings:
    configFilePath: Optional[str] = None
    application: ApplicationSettings = field(default_factory=ApplicationSettings)
    storage: StorageSettings = field(default_factory=StorageSettings)
    

