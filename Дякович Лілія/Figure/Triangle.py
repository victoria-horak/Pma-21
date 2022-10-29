from Figure import Figure
from NotExistException import NotExistException


class Triangle(Figure):
    def __init__(self, Color, a, b, c):
        Figure.__init__(self, Color)
        if (a + b) > c and (b + c) > a and (a + c) > b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise NotExistException("Triangle does not exist")

    def perum(self):
        return self.a + self.b + self.c

    def square(self):
        p = Triangle.perum(self) / 2
        return round(((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5), 2)

    def print(self):
        print("Triangle :")
        Figure.print(self)
