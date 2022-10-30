from Exception import WrongLength
import math as m
from Figure import *


class Circle(Figure):
    def __init__(self, colour, r):
        super().__init__(colour)
        if r > 0:
            self.r = r
        else:
            raise WrongLength("Length is less than 0 in circle.")
        self.colour = colour

    def find_area(self):
        return round((m.pi * self.r * self.r), 1)

    def show(self):
        print(self.colour.colour + ' Circle: ')

    def find_perimeter(self):
        return round((2 * m.pi * self.r), 1)
