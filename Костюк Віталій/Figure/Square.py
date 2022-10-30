from Rectangle import *
from Figure import *
from Color import *
from IncorrectData import *


class Square(Rectangle):
    type = "Square"

    def getType(self):
        return self.type

    def __init__(self, color: Color, side: int):
        if side >= 0:
            Rectangle.__init__(self, color, side, side)
        else:
            raise IncorrectData("Incorrect data for square")

    def Perimeter(self):
        return Rectangle.Perimeter(self)

    def Area(self):
        return Rectangle.Area(self)

    def __str__(self):
        return Figure.__str__(self)
