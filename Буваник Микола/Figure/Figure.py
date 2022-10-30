from Colour import *


class Figure:
    def __init__(self, colour: Colour):
        self.colour = colour

    def Perimetr(self):
        pass

    def Area(self):
        pass

    def getType(self):
        pass

    def __str__(self):
        info = "Figure type:" + self.getType()+"\n"
        info += "Color:" + str(self.colour.getColour()) + "\n"
        info += "Perimetr = " + str(self.Perimetr()) + "\n"
        info += "Area = " + str(self.Area()) + "\n"
        return info
