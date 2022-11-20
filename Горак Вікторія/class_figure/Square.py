from Rectangle import *
from Exception import WrongLength


class Square(Rectangle):
    def __init__(self, colour, a):
        if a > 0:
            self.a = a
            super().__init__(colour, a, a)
            self.colour = colour
        else:
            raise WrongLength("Length is less than 0 in square. ")

    def show(self):
        print(self.colour.colour + ' Square:')
