from Figure import *
from math import *
import turtle


class WrongParameters(Exception):
    pass


class Triangle(Figure):

    def __init__(self, color: Color = Blue(), firstSide=0, secondSide=0, thirdSide=0):
        try:
            if firstSide + secondSide <= thirdSide or firstSide + thirdSide <= secondSide or secondSide + thirdSide <= firstSide or firstSide <= 0 or secondSide <= 0 or thirdSide <= 0:
                raise WrongParameters
            self.firstSide = firstSide
            self.secondSide = secondSide
            self.thirdSide = thirdSide
        except WrongParameters:
            print("wrong parameters")
            exit(1)
        except ValueError:
            print("Value error")
            exit(1)
        self.color = color

    def __str__(self):
        result = "Triangle:" + '\n'
        result += "side 1: " + str(self.firstSide) + " side 2: " + str(self.secondSide) + " side 3: " + str(
            self.thirdSide) + '\n'
        result += "color: " + self.color.getColor() + '\n'
        result += "perimeter: " + str(self.perimeter()) + '\n'
        result += "area: " + str(self.area()) + '\n'
        return result

    def perimeter(self):
        return self.firstSide + self.secondSide + self.thirdSide

    def area(self):
        p = self.perimeter() / 2
        result = (p * (p - self.firstSide) * (p - self.secondSide) * (p - self.thirdSide)) ** 0.5
        return result

    def angle(self, firstSide, secondSide, thirdSide):
        return degrees(acos((secondSide ** 2 + thirdSide ** 2 - firstSide ** 2) / (
                2.0 * secondSide * thirdSide)))

    def canDraw (self):
        return self.firstSide + self.secondSide > self.thirdSide and self.secondSide + self.thirdSide > self.firstSide \
               and self.thirdSide + self.firstSide > self.secondSide

    def draw(self):
        turtle.color(self.color.getColor())
        if self.firstSide == self.secondSide == self.thirdSide:
            for i in range(3):
                turtle.forward(self.firstSide)
                turtle.left(120)
        elif not self.canDraw():
            print("this triangle can't be drawn")
        else:
            turtle.forward(self.thirdSide)
            turtle.left(180 - self.angle(self.secondSide, self.thirdSide, self.firstSide))
            turtle.forward(self.firstSide)
            turtle.left(180 - self.angle(self.thirdSide, self.firstSide, self.secondSide))
            turtle.forward(self.secondSide)
        time.sleep(3)
        turtle.Screen().reset()
