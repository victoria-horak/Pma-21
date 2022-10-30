from Rectangle import *
from Square import *
from Circle import *
from Triangle import *

square = Square("blue", 100)
print(square)
square.draw()

circle = Circle("green", 50)
print(circle)
circle.draw()

rectangle = Rectangle("purple", 50, 20)
print(rectangle)
rectangle.draw()

triangle = Triangle("blue", 60, 60, 60)
print(triangle)
triangle.draw()
