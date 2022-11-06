from ClassShape import Shape
from ClassColor import *
import math
from InvalidSizes import *


class Triangle(Shape):
    def __init__(self, first, second, third, color: Color):
        Shape.__init__(self, color)
        if (first + second > third and
                first + third > second and
                second + third > first):
            self.first = first
            self.second = second
            self.third = third
        else:
            raise InvalidSizes("The dimensions entered for Triangle are invalid!")
            first = 1
            second = 1
            third = 1

    def square(self):
        p = (self.first + self.second + self.third) / 2
        return round(math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)), 2)

    def perimeter(self):
        return self.first + self.second + self.third

    def show(self):
        print("Triangle: a = %d, b = %d, c = %d" % (self.first, self.second, self.third))
        print("Color of triangle: ", self.color.printColor(self))
        print("Square = ", self.square())
        print("Perimeter = ", self.perimeter())