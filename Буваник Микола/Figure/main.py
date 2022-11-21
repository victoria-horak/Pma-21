from Circle import Circle
from Triangle import Triangle
from Rectangle import Rectangle
from Square import Square
from Green import *
from Blue import *
from Yellow import *

yellow = Yellow
blue = Blue
green = Green
triangle = Triangle(yellow, 4.3, 5.2, 3)
circle = Circle(green, 3)
rectangle = Rectangle(blue, 3, 4)
square = Square(blue, 3)
print(triangle, circle, rectangle, square, sep="\n")
