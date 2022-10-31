from Figurs import *
from math import acos, degrees


class Triangle(Figur):
    def __init__(self, color: Color = Black(), firstSide=1, secondSide=1, thirdSide=1):
        Figur.__init__(self, color)
        if firstSide < 0 or secondSide < 0 or thirdSide < 0:
            raise DifferentError("the sides of a triangle cannot be negative.")
        if not (firstSide + secondSide >= thirdSide and secondSide + thirdSide >= firstSide and thirdSide + firstSide >= secondSide):
            raise DifferentError("according to the dimensions that you have given, a triangle will not turn out.")
        self.firstSide = firstSide
        self.secondSide = secondSide
        self.thirdSide = thirdSide

    def __str__(self):
        return f"Triangle:\ncolor = {self.color.getColor()}\nfirst side = {self.firstSide}\nsecond side = {self.secondSide}" \
               f"\nthird side = {self.thirdSide}\nperimeter = {self.perimeter()}\nsquare = {self.square()}\n"

    def perimeter(self):
        return self.firstSide + self.secondSide + self.thirdSide

    def square(self):
        halfPerimeter = self.perimeter() / 2
        return ((halfPerimeter * (halfPerimeter - self.firstSide) * (halfPerimeter - self.secondSide) * (
                halfPerimeter - self.thirdSide)) ** 0.5)

    @classmethod
    def triangle_angle(cls, firstSide, secondSide, thirdSide):
        return degrees(acos((secondSide ** 2 + thirdSide ** 2 - firstSide ** 2) / (2.0 * secondSide * thirdSide)))

    def triangle_exists(self):
        return self.firstSide + self.secondSide > self.thirdSide and self.secondSide + self.thirdSide > self.firstSide \
               and self.thirdSide + self.firstSide > self.secondSide

    def draw(self):
        if not self.triangle_exists():
            print("Program can`t draw such triangle.")
            return
        color(self.color.getColor())
        begin_fill()
        forward(self.thirdSide * 15)
        left(180 - Triangle.triangle_angle(self.secondSide, self.thirdSide, self.firstSide))
        forward(self.firstSide * 15)
        left(180 - Triangle.triangle_angle(self.thirdSide, self.firstSide, self.secondSide))
        forward(self.secondSide * 15)
        end_fill()
        time.sleep(7)
        turtle.Screen().reset()
