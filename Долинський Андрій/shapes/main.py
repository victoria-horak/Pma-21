from rectangle import Rectangle
from triangle import Triangle
from square import Square
from circle import Circle
from red import Red
from blue import Blue
from purple import Purple
from green import Green

from doesntExistException import doesntExistException

try:
    rectangle = Rectangle(Blue, 2, 4)
    rectangle.print()

    triangle = Triangle(Green, 3, 4, 5)
    triangle.print()

    square = Square(Purple, 5)
    square.print()

    circle = Circle(Red, 9)
    circle.print()
except doesntExistException as error:
    print(error)
