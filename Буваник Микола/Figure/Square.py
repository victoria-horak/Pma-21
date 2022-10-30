from Rectangle import Rectangle
from Figure import Figure
from Colour import Colour


class Square(Rectangle):
    type = "Square"

    def __init__(self, colour: Colour, a):
        Rectangle.__init__(self,colour, a, a)

    def Perimetr(self):
        return Rectangle.Perimetr(self)

    def getType(self):
        return self.type

    def Area(self):
        return Rectangle.Area(self)

    def __str__(self):
        return Figure.__str__(self)
