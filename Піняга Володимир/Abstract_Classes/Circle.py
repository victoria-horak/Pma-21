from ClassShape import Shape
from ClassColor import *
import math
from InvalidSizes import *


class Circle(Shape):
    def __init__(self, radius, color: Color):
        Shape.__init__(self, color)
        if radius > 0:
            self.radius = radius
        else:
            raise InvalidSizes("The dimensions entered for Circle are invalid!")

    def square(self):
        return round(math.pi * pow(self.radius, 2), 2)

    def perimeter(self):  # length of circle
        return round(2 * math.pi * self.radius, 2)

    def show(self):
        print("Circle: R = %d" % self.radius)
        print("Color of circle: ", self.color.printColor(self))
        print("Square = ", self.square())
        print("Length = ", self.perimeter())
