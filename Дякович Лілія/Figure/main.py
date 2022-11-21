from Rectangle import Rectangle
from Triangle import Triangle
from Square import Square
from Circle import Circle
from BlueColor import Blue
from NotExistException import NotExistException
from GreenColor import Green
from YellowColor import Yellow
from PinkColor import Pink

try:
    rectangle = Rectangle(Blue, 2, 4)
    rectangle.print()

    triangle = Triangle(Green, 3, 4, 5)
    triangle.print()

    square = Square(Pink, 5)
    square.print()

    circle = Circle(Yellow, 9)
    circle.print()
except NotExistException as e:
    print(e)
