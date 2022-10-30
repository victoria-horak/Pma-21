from Figure import *


class Circle(Figure):
    type = "Circle"

    def __init__(self, colour: Colour, a):
        Figure.__init__(self, colour)
        self.a = a

    def Perimetr(self):
        return 2*3.14*self.a

    def getType(self):
        return self.type

    def Area(self):
        return 3.14*(self.a**2)

    def __str__(self):
        return Figure.__str__(self)
