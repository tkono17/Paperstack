
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
