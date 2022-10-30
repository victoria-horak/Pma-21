from Figure import *
from Circle import *
from Triangle import *
from Square import *
from Rectangle import *
from Colour import *
from Blue import *
from Green import *
from Yellow import *

try:
    circle = Circle(Blue(), 5)
    circle.show()
    print('Area of circle:', circle.find_area())
    print('Perimeter of circle:', circle.find_perimeter())
except WrongLength as error:
    print(error)

try:
    triangle = Triangle(Yellow(), 4, 6, 8)
    triangle.show()
    print('Area of triangle:', triangle.find_area())
    print('Perimeter of triangle:', triangle.find_perimeter())
except WrongLength as error:
    print(error)

try:
    square = Square(Green(), 3)
    square.show()
    print('Area of square:', square.find_area())
    print('Perimeter of square:', square.find_perimeter())
except WrongLength as error:
    print(error)

try:
    rectangle = Rectangle(Blue(), 7, 6)
    rectangle.show()
    print('Area of rectangle:', rectangle.find_area())
    print('Perimeter of rectangle:', rectangle.find_perimeter())
except WrongLength as error:
    print(error)
