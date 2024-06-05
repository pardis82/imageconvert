from .picture import Picture

class Circle(Picture):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14*(self.radius**2)