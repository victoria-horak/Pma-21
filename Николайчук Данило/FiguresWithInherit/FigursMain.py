from Figurs import *
from Circle import Circle
from Triangle import Triangle
from Square import Square
from Rectangle import Rectangle

triangle = Triangle(Red())
print(triangle)
triangle.draw()

square = Square(Blue())
print(square)
square.draw()

circle = Circle(Green())
print(circle)
circle.draw()

rectangle = Rectangle(Yellow())
print(rectangle)
rectangle.draw()
