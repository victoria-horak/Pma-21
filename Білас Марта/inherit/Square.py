from Rectangle import *


class Square(Rectangle):

    def __init__(self, color: Color = Blue(), side=0):
        Rectangle.__init__(self, color, side, side)

    def __str__(self):
        result = "Square:" + '\n'
        result += "side : " + str(self.firstSide) + '\n'
        result += "color: " + self.color.getColor() + '\n'
        result += "perimeter: " + str(self.perimeter()) + '\n'
        result += "area: " + str(self.area()) + '\n'
        return result
