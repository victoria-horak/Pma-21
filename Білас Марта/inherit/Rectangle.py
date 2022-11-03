from Figure import *
import turtle


class WrongParameters(Exception):
    pass


class Rectangle(Figure):

    def __init__(self, color: Color = Blue(), firstSide=0, secondSide=0):
        try:
            if firstSide <= 0 or secondSide <= 0:
                raise WrongParameters
            self.firstSide = firstSide
            self.secondSide = secondSide
        except ValueError:
            print("this value must be number")
        except WrongParameters:
            print("wrong parameters")
        self.color = color

    def __str__(self):
        result = "Rectangle:" + '\n'
        result += "side 1: " + str(self.firstSide) + " side 2: " + str(self.secondSide) + '\n'
        result += "color: " + self.color.getColor() + '\n'
        result += "perimeter: " + str(self.perimeter()) + '\n'
        result += "area: " + str(self.area()) + '\n'
        return result

    def perimeter(self):
        return 2 * (self.firstSide + self.secondSide)

    def area(self):
        return self.firstSide * self.secondSide

    def draw(self):
        turtle.color(self.color.getColor())
        for i in range(2):
            turtle.forward(self.firstSide)
            turtle.right(90)
            turtle.forward(self.secondSide)
            turtle.right(90)
        time.sleep(3)
        turtle.Screen().reset()
