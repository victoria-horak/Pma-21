from ClassColor import Color
from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, first, color: Color):
        Rectangle.__init__(self, first, first, color)

    def show(self):
        print("Square: a = %d" % self.first)
        print("Color of square: ", self.color.printColor(self))
        print("Square = ", self.square())
        print("Perimeter = ", self.perimeter())
