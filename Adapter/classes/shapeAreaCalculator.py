from classes.picture import Picture
from classes.circle import Circle
from classes.rectangle import Rectangle

class ShapeAreaCalculator:

    def __init__(self,picture):
        if not isinstance(picture,Picture):
            raise TypeError("Input is not a picture!")
        self.picture = picture

    def calculate(self):
        if isinstance(self.picture,Circle):
            return 'Area of '+ self.picture.name + ' is: ' + self.CircleAdapter(self.picture).get_area()
        elif isinstance(self.picture,Rectangle):
            return 'Area of '+ self.picture.name + ' is: ' + self.RectangleAdapter(self.picture).get_area()
        else:
            raise NotImplementedError('There is no adapter for the input!')

    class CircleAdapter:
        
        def __init__(self,circle):
            if not isinstance(circle,Circle):
                raise TypeError("input is not a circle!")
            self.circle = circle    

        def get_area(self):
            return str(self.circle.area())
        

    class RectangleAdapter:
        
        def __init__(self,rectangle):
            if not isinstance(rectangle,Rectangle):
                raise TypeError("input is not a rectangle!")
            self.rectangle = rectangle    

        def get_area(self):
            return str(self.rectangle.area())
        