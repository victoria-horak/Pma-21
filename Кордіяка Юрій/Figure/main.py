from Colour import *
from Figure import *

blue = Blue
yellow = Yellow
green = Green

try:
    triangle = Triangle(green, 5, 4, 3)
    triangle.showInformation()
    print(triangle.perimeter())
    print(triangle.area())
    triangle1 = Triangle(yellow, 5, 4, 3)
    triangle1.showInformation()
    print(triangle1.area())
except ExceptionTriangleNotExist as exception:
    print(exception)

try:
    rectangle = Rectangle(green, 3, 4)
    rectangle.showInformation()
    print(rectangle.area())
    print(rectangle.perimeter())
except ExceptionSideisLessZero as exception:
    print(exception)


try:
    square = Square(blue, 3)
    square.showInformation()
    print(square.area())
    print(square.perimeter())
except ExceptionSideisLessZero as exception:
    print(exception)


