from Figure import *

class Rectangle(Figure):
    type = "Rectangle"

    def __init__(self, colour: Colour, a, b):
        Figure.__init__(self, colour)
        self.a = a
        self.b = b

    def Perimetr(self):
        return (self.a + self.b)*2

    def getType(self):
        return self.type

    def Area(self):

        return self.a*self.b

    def __str__(self):
        return Figure.__str__(self)