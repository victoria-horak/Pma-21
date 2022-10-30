from Figure import *
from IncorrectData import *


class Rectangle(Figure):
    type = "Rectangle"

    def getType(self):
        return self.type

    def __init__(self, color, length, width):
        if length >= 0 and width >= 0:
            Figure.__init__(self, color)
            self.length = length
            self.width = width
        else:
            raise IncorrectData("Incorrect data for rectangle")

    def Perimeter(self):
        return (self.length + self.width) * 2

    def Area(self):
        return self.length * self.width

    def __str__(self):
        return Figure.__str__(self)
