from Figure import *
from Exception import WrongLength


class Triangle(Figure):
    def __init__(self, colour, a, b, c):
        super().__init__(colour)
        if a > 0 and b > 0 and c > 0:
            if (a + b) > c and (b + c) > a and (a + c) > b:
                self.a = a
                self.b = b
                self.c = c
            else:
                raise WrongLength("Incorrect data")
        else:
            raise WrongLength("Length is less than 0 in triangle.")
        self.colour = colour

    def find_area(self):
        p = round((self.a + self.b + self.c) / 2, 4)
        area = round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5, 4)
        return area

    def show(self):
        print(self.colour.colour + ' Triangle: ')

    def find_perimeter(self):
        return self.a + self.b + self.c
