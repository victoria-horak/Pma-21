from Circle import *
from Rectangle import *
from Square import *
from Triangle import *

circle1 = Circle(Yellow(), 100)
print(circle1)
circle1.paint()

rectangle1 = Rectangle(Blue(), 100,20)
print(rectangle1)
rectangle1.paint()

square1 = Square(Green(), 200)
print(square1)
square1.paint()

triangle1 = Triangle(Green(), 100, 200, 250)
print(triangle1)
triangle1.paint()
