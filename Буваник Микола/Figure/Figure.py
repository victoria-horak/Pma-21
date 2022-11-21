from Colour import *
from abc import *


class Figure(ABC):
    def __init__(self, colour: Colour):
        self.colour = colour

    @abstractmethod
    def Perimetr(self):
        pass

    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def getType(self):
        pass

    @abstractmethod
    def __str__(self):
        info = "Figure type:" + self.getType() + "\n"
        info += "Color:" + str(self.colour.getColour(self)) + "\n"
        info += "Perimetr = " + str(self.Perimetr()) + "\n"
        info += "Area = " + str(self.Area()) + "\n"
        return info
