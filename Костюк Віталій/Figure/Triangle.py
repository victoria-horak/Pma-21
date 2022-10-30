from Figure import *
from SideLengthError import *
from IncorrectData import *


class Triangle(Figure):
    type = "Triangle"

    def getType(self):
        return self.type

    def __init__(self, color: Color, a: int, b: int, c: int):
        if a >= 0 and b >= 0 and c >= 0:
            Figure.__init__(self, color)
            if c > a+b or a > b+c or b > a+c:
                raise SideLengthError("Triangle with such sides does not exist")
            else:
                self.a = a
                self.b = b
                self.c = c
        else:
            raise IncorrectData("Incorrect data for triangle")

    def Perimeter(self):
        return self.a + self.b + self.c

    def Area(self):
        half_p = self.Perimeter() / 2
        area = round((half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)) ** 0.5, 2)
        return area

    def __str__(self):
        return Figure.__str__(self)