from abc import ABC, abstractmethod
from Color import Color
import math
from IncorrectSize import IncorrectSize


class Shape(ABC):
    @abstractmethod
    def __init__(self, Color):
        self.Color = Color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perymetr(self):
        pass


class Triangle(Shape):
    def __init__(self, firstSide, secondSide, thirdSide, Color):
        Shape.__init__(self, Color)
        if (
                firstSide + secondSide > thirdSide and secondSide + thirdSide > firstSide and firstSide + thirdSide > secondSide):
            self.firstSide = firstSide
            self.secondSide = secondSide
            self.thirdSide = thirdSide
        else:
            raise IncorrectSize("Sides are not correct")

    def area(self):
        pivperymetr = (self.firstSide + self.secondSide + self.thirdSide) / 2
        area = math.sqrt(pivperymetr * (pivperymetr - self.firstSide) * (pivperymetr - self.secondSide) * (
                pivperymetr - self.thirdSide))
        return area

    def perymetr(self):
        return (self.firstSide + self.secondSide + self.thirdSide)

    def output(self):
        print("Triangle of " + self.Color.getColor() + " color with sides: a = " + str(self.firstSide) + ", b = " + str(
            self.secondSide) + ", c = " + str(self.thirdSide))
        print("Area: " + str(self.area()))
        print("Perymetr: " + str(self.perymetr()))


class Rectangle(Shape):
    def __init__(self, firstSide, secondSide, Color):
        Shape.__init__(self, Color)
        if (firstSide > 0 and secondSide > 0):
            self.firstSide = firstSide
            self.secondSide = secondSide
        else:
            raise IncorrectSize("Sides are not correct")

    def area(self):
        return self.secondSide * self.firstSide

    def perymetr(self):
        return 2 * (self.firstSide + self.secondSide)

    def output(self):
        print(
            "Rectangle of " + self.Color.getColor() + " color with sides: a = " + str(self.firstSide) + ", b = " + str(
                self.secondSide))
        print("Area: " + str(self.area()))
        print("Perymetr: " + str(self.perymetr()))


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side, Color)

    def output(self):
        print(
            "Square of " + self.Color.getColor() + " color with side: a = " + str(self.firstSide))
        print("Area: " + str(self.area()))
        print("Perymetr: " + str(self.perymetr()))


class Circle(Shape):
    def __init__(self, radius, Color):
        Shape.__init__(self, Color)
        if radius > 0:
            self.radius = radius
        else:
            raise IncorrectSize("Radius is not correct")

    def area(self):
        return (math.pi * (self.radius) * (self.radius))

    def perymetr(self):
        return (2 * math.pi * self.radius)

    def output(self):
        print(
            "Circle of " + self.Color.getColor() + " color with radius: r = " + str(self.radius))
        print("Area: " + str(self.area()))
        print("Perymetr: " + str(self.perymetr()))
