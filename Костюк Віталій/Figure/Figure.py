from Color import *


class Figure:
    def __init__(self, colour):
        self.colour = colour

    def Perimeter(self):
        pass

    def Area(self):
        pass

    def getType(self):
        pass

    def __str__(self):
        figure_str = "Type of figure : " + str(self.getType()) + "\n"
        figure_str += "Color:" + str(self.colour.getColor()) + "\n"
        figure_str += "Perimetr = " + str(self.Perimeter()) + "\n"
        figure_str += "Area = " + str(self.Area()) + "\n"
        return figure_str
