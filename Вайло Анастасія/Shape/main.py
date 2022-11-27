from Circle import Circle
from Triangle import Triangle
from Rectangle import Rectangle
from Square import Square
from Colors import *
from InvalidShapeException import *

try:
    triangle = Triangle(Blue, 6, 8, 10)
    triangle.print_info()
except InvalidShapeException as e:
    print(str(e))

try:
    circle = Circle(Red, 6)
    circle.print_info()
except InvalidShapeException as e:
    print(str(e))

try:
    rectangle = Rectangle(Yellow, 12, 3)
    rectangle.print_info()
except InvalidShapeException as e:
    print(str(e))

try:
    square = Square(Green, 3)
    square.print_info()
except InvalidShapeException as e:
    print(str(e))
