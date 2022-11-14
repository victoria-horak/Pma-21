from ClassFigures import *
from Invalid import Invalid

try:
    greenColor = Green()
    blueColor = Blue()
    yellowColor = Yellow()
    orangeColor = Orange()

    square = Square(3, greenColor)
    print("Square:\n Color:", square.getColor())
    print("Perimetr:", square.perimeter())
    print("Area:", square.area(), "\n")

    rectangle = Rectangle(3, 6, orangeColor)
    print("Rectangle:\n Color:", rectangle.getColor())
    print("Perimetr:", rectangle.perimeter())
    print("Area:", rectangle.area(), "\n")

    circle = Circle(5, yellowColor)
    print("Circle:\n Color:", circle.getColor())
    print("Perimetr:", circle.perimeter())
    print("Area:", circle.area(), "\n")

    triangle = Triangle(3, 4, 5, blueColor)
    print("Triangle:\n Color:", triangle.getColor())
    print("Perimetr:", triangle.perimeter())
    print("Area:", triangle.area())

except Invalid as e:
    print(e)
