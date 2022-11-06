from ClassShape import Shape
from ClassColor import *
from InvalidSizes import *


class Rectangle(Shape):
    def __init__(self, first, second, color: Color):
        Shape.__init__(self, color)
        self.first = first
        self.second = second

    def perimeter(self):
        return (self.first + self.second)*2

    def square(self):
        space = self.first * self.second
        return space

    def show(self):
        print("Rectangle: a = %d, b = %d" % (self.first, self.second))
        print("Color of Rectangle: ", self.color.printColor(self))
        print("Square = ", self.square())
        print("Perimeter = ", self.perimeter())

