from Rectangle import *
from Square import *
from Circle import *
from Triangle import *

square = Square(Blue(), 100)
print(square)
square.draw()
square.changeColor("purple")
square.draw()

circle = Circle(Green(), 50)
print(circle)
circle.draw()

rectangle = Rectangle(Purple(), 50, 20)
print(rectangle)
rectangle.draw()

triangle = Triangle(Blue(), 30, 40, 50)
print(triangle)
triangle.draw()
