from Figure import *
from IncorrectData import *


class Circle(Figure):
    type = "Circle"

    def getType(self):
        return self.type

    def __init__(self, color: Color, radius: int):
        Figure.__init__(self, color)
        if radius >= 0:
            self.radius = radius
        else:
            raise IncorrectData("Incorrect data for circle")

    def Perimeter(self):
        return 2 * 3.14 * self.radius

    def Area(self):
        return 3.14 * (self.radius ** 2)

    def __str__(self):
        return Figure.__str__(self)
