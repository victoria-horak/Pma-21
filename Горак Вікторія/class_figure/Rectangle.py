from Exception import WrongLength
from Figure import *


class Rectangle(Figure):
    def __init__(self, colour, a, b):
        super().__init__(colour)
        if a > 0 and b > 0:
            self.a = a
            self.b = b
        else:
            raise WrongLength("Length is less than 0 in rectangle.")
        self.colour = colour

    def find_area(self):
        return self.a * self.b

    def show(self):
        print(self.colour.colour + ' Rectangle: ')

    def find_perimeter(self):
        return 2 * (self.a + self.b)
