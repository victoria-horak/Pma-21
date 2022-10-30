from ClassColor import *
from ClassShape import *
from InvalidSizes import *


triangle = Triangle(2, 3, 4, 'Green')
triangle.show()
print("==================================")
circle = Circle(4, 'Blue')
circle.show()
print("==================================")
rectangle = Rectangle(5, 8, 'Yellow')
rectangle.show()
print("==================================")
square = Square(4)
square.color = 'Green'
square.show()