<<<<<<< HEAD:backend/src/paperstack_server/utils/stores.py
import logging

log = logging.getLogger(__name__)

class Store:
    def __init__(self):
        self.names = []
        self.nameToId = {}
        self.idToName = {}
        self.idToX = {}

    def exists(self, name):
        if name in self.names:
            return True
        return False

    def find(self, nameOrId):
        x = None
        if self.exists(name):
            id = nameOrId
            if type(nameOrId) != 'int':
                id = self.nameToId(nameOrId)
            x = self.idToX[id]
        return x

    def add(self, name, id, x):
        if name not in self.names:
            self.names.append(key)
            self.nameToId[name] = id
            self.idToName[id] = name
            self.idToX[id] = x
        else:
            id1 = self.nameToId[name]
            log.warning(f'Object with name {name} is already registered with id={id1}, tried to register with id={id}')
            
    def clear(self):
        self.names.clear()
        self.nameToId.clear()
        self.idToName.clear()
        self.idToX.clear()
            
        
class QueryStore(Store):
    def __init__(self):
        super().__init__()
        pass

    def init(self):
        pass
    
class DocTypeStore(Store):
    def __init__(self):
        super().__init__()
        pass

    def init(self):
        self.add('Article', 1)
        self.add('Eprint', 2)
        self.add('Thesis', 3)
        self.add('ThesisD', 4)
        self.add('ThesisM', 5)
        self.add('ThesisB', 6)
        self.add('Presentation', 7)
        self.add('Manual', 8)
        self.add('Specification', 9)
        self.add('Tutorial', 10)
        self.add('TechnicalNote', 11)
        self.add('Datasheet', 12)
        self.add('Review', 13)
        self.add('Book', 14)
        
=======
import logging

log = logging.getLogger(__name__)

class Store:
    def __init__(self):
        self.names = []
        self.nameToId = {}
        self.idToName = {}
        self.idToX = {}

    def exists(self, name):
        if name in self.names:
            return True
        return False

    def find(self, nameOrId):
        x = None
        id = 0
        name = ''
        if type(nameOrId) != 'int':
            name = nameOrId
            id = self.nameToId(nameOrId)
        elif type(nameOrId) == 'int':
            id = nameOrId
            name = self.idToName[nameOrId]
        if name != '' and self.exists(name):
            x = self.idToX[id]
        return x

    def size(self):
        return len(self.names)
    
    def add(self, name, id, x=None):
        if name not in self.names:
            self.names.append(name)
            self.nameToId[name] = id
            self.idToName[id] = name
            self.idToX[id] = x
        else:
            id1 = self.nameToId[name]
            log.warning(f'Object with name {name} is already registered with id={id1}, tried to register with id={id}')
            
    def clear(self):
        self.names.clear()
        self.nameToId.clear()
        self.idToName.clear()
        self.idToX.clear()
            
        
>>>>>>> e77b56f8ec3a102cd20e7f214f11504fca852081:backend/src/appbasics/model/store.py
