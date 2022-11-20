from shape import Shape
from doesntExistException import doesntExistException
from colors import Color


class Triangle(Shape):
    def __init__(self, Color, a, b, c):
        Shape.__init__(self, Color)
        if (a + b) > c and (b + c) > a and (a + c) > b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise doesntExistException("Triangle does not exist")

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = Triangle.perimeter(self) / 2
        return round(((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5), 2)

    def print(self):
        print("Triangle :")
        Shape.print(self)
