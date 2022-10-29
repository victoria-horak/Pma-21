from error import Error
from shape import *
from bridge import *


try:
    circle = Circle(5, Purple)
    circle.print()
    circle = Circle(3, Blue)
    circle.print()

    square = Square(2, Green)
    square.print()
    square = Square(45, Yellow)
    square.print()

    triangle = Triangle(3, 4, 5, Orange)
    triangle.print()

    rectangle = Rectangle(5, 6, Red)
    rectangle.print()

except Error as e:
    print(e)

