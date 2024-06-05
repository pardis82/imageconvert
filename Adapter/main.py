from classes.picture import Picture
from classes.circle import Circle
from classes.rectangle import Rectangle
from classes.shapeAreaCalculator import ShapeAreaCalculator


# Define Shapes
circle_1 = Circle(name='Circle 1',radius=2)
rectangle_1 = Rectangle(name='Rectangle 1',width=2,length=3)

# Area calculator
print(ShapeAreaCalculator(circle_1).calculate())
print(ShapeAreaCalculator(rectangle_1).calculate())

