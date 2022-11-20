import math as m
from Figure import *
from Exception import WrongLength


class Circle(Figure):
    def __init__(self, colour, radius):
        super().__init__(colour)
        if radius > 0:
            self.radius = radius
        else:
            raise WrongLength("Length is less than 0 in circle.")
        self.colour = colour

    def find_area(self):
        return round((m.pi * self.radius * self.radius), 1)

    def show(self):
        print(self.colour.colour + ' Circle: ')

    def find_perimeter(self):
        return round((2 * m.pi * self.radius), 1)
