from ..model import Store

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
        
