from rectangle import Rectangle
from colors import Color


class Square(Rectangle):
    def __init__(self, Color, a):
        Rectangle.__init__(self, Color, a, a)

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return self.a * 4

    def print(self):
        print("Square :\nperimeter = ", self.perimeter(), "  square = ", self.area(), "  color = ",
              self.color.printColor(self), "\n")
