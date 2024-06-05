from .picture import Picture

class Rectangle(Picture):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width  = width
    
    def area(self):
        return self.width * self.length
