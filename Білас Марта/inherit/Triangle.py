from Figure import *
import math
import turtle


class WrongParameters(Exception):
    pass


class Triangle(Figure):

    def __init__(self, color: Color = "blue", firstSide=0, secondSide=0, thirdSide=0):
        try:
            if firstSide + secondSide <= thirdSide or firstSide + thirdSide <= secondSide or secondSide + thirdSide <= firstSide or firstSide <= 0 or secondSide <= 0 or thirdSide <= 0:
                raise WrongParameters
            self.firstSide = firstSide
            self.secondSide = secondSide
            self.thirdSide = thirdSide
        except WrongParameters:
            print("wrong parameters")
        except ValueError:
            print("Value error")
        self.color = Color(color)

    def __str__(self):
        result = "Triangle:" + '\n'
        result += "side 1: " + str(self.firstSide) + " side 2: " + str(self.secondSide) + "side 3: " + str(
            self.thirdSide) + '\n'
        result += "color: " + self.color.getColor() + '\n'
        result += "perimeter: " + str(self.perimeter()) + '\n'
        result += "area: " + str(self.area())
        return result

    def perimeter(self):
        return self.firstSide + self.secondSide + self.thirdSide

    def area(self):
        p = self.perimeter() / 2
        result = math.sqrt(p * (p - self.firstSide) * (p - self.secondSide) * (p - self.thirdSide))
        return result

    def draw(self):
        turtle.color(self.color.getColor())
        turtle.forward(self.firstSide)
        turtle.left(120)
        turtle.forward(self.secondSide)
        turtle.left(120)
        turtle.forward(self.thirdSide)
        turtle.Screen().reset()
