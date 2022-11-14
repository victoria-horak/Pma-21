from Shape import *
from Color import *


if __name__ == "__main__":
    blue = Blue()
    green = Green()
    yellow = Yellow()

    triangle = Triangle(5, 10, 13, blue)
    circle = Circle(yellow, 5)
    square = Square(green, 10)
    rectangle = Rectangle(20, 10, blue)

    triangle.show()
    circle.show()
    square.show()
    rectangle.show()
