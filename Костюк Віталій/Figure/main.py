from Figure import *
from Circle import Circle
from Triangle import Triangle
from Rectangle import Rectangle
from Square import Square
from SideLengthError import *
from IncorrectData import *


counter_for_triangle = 0
counter_for_circle = 0
counter_for_rectangle = 0
counter_for_square = 0


circle_radius = int(input("Circle radius = "))
#  Circle
try:
    circle = Circle(Yellow, circle_radius)
except IncorrectData as e:
    print(e)
    counter_for_circle += 1
if counter_for_circle == 0:
    circle = Circle(Yellow, circle_radius)
    print(circle)
    print()


#  Rectangle
rectangle_length = int(input("Rectangle length = "))
rectangle_width = int(input("Rectangle width = "))
try:
    rectangle = Rectangle(Green, rectangle_length, rectangle_width)
except IncorrectData as e:
    print(e)
    counter_for_rectangle += 1
if counter_for_rectangle == 0:
    rectangle = Rectangle(Green, rectangle_length, rectangle_width)
    print(rectangle)
    print()

#  Square
square_side = int(input("Square side = "))
try:
    square = Square(Blue, square_side)
except IncorrectData as e:
    print(e)
    counter_for_square += 1
if counter_for_square == 0:
    square = Square(Blue, square_side)
    print(square)
    print()

#  Triangle
triangle_a = int(input("Triangle a = "))
triangle_b = int(input("Triangle b = "))
triangle_c = int(input("Triangle c = "))
try:
    try:
        triangle = Triangle(Blue, triangle_a, triangle_b, triangle_c)
    except SideLengthError as e:
        print(e)
        counter_for_triangle += 1
except IncorrectData as e:
    print(e)
    counter_for_triangle += 1
if counter_for_triangle == 0:
    triangle = Triangle(Blue, triangle_a, triangle_b, triangle_c)
    print(triangle)
    print()
