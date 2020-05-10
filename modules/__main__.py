#__main__

class Object: #base class
    def __init__(self):
        self.name = "Item"
        self.cost = 0
        self.saleValue = 0

class Materials(Object):
    def __init__(self):
        Object.__init__(self)

class Product(Object):
    def __init__(self):
        Object.__init__(self)

class Tool(Object):
    def __init__(self):
        Object.__init__(self)

