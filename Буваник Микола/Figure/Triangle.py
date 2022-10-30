from Figure import *
from SideTriangleExeption import SideTriangleExeption

class Triangle(Figure):
    type = "Triangle"

    def __init__(self, colour: Colour, a, b, c):
        Figure.__init__(self, colour)
        if c > a + b or a > b + c or b > a + c:
            raise SideTriangleExeption("Sum two side in triangle need beggest than third side")
        else:
            self.a = a
            self.b = b
            self.c = c

    def Perimetr(self):
        return self.a + self.b + self.c

    def getType(self):
        return self.type

    def Area(self):
        p = self.Perimetr() / 2
        area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return round(area, 2)

    def __str__(self):
        return Figure.__str__(self)
