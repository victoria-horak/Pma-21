from Shape import *
from Color import *
from IncorrectSize import IncorrectSize

Green = Green()
Blue = Blue()
Yellow = Yellow()
Red = Red()

try:
    print("\n")
    triangle = Triangle(5, 7, 8, Green)
    triangle.output()
    print("\n")
    rectangle = Rectangle(10, 8, Red)
    rectangle.output()
    print("\n")
    square = Square(12)
    square.Color = Blue
    square.output()
    print("\n")
    square = Circle(6, Yellow)
    square.output()
except IncorrectSize as e:
    print(e)
