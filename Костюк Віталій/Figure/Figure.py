from Color import *


class Figure:
    def __init__(self, color: Color):
        self.color = color

    def Perimeter(self):
        pass

    def Area(self):
        pass

    def getType(self):
        pass

    def __str__(self):
        figure_str = "Type of figure : " + str(self.getType()) + "\n" + "Color:" + \
                     str(self.color.getColor()) + "\n" + "Perimeter = " + \
                     str(self.Perimeter()) + "\n" + "Area = " + str(self.Area()) + "\n"
        return figure_str
