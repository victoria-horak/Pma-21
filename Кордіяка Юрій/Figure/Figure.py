from abc import abstractmethod, ABC
from Colour import Colour
from ExceptionTriangleNotExist import ExceptionTriangleNotExist
from ExceptionSideisLessZero import ExceptionSideisLessZero


class Figure(ABC):
    @abstractmethod
    def __init__(self, Colour):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def showInformation(self):
        pass


class Triangle(Figure):
    def __init__(self, Colour, a, b, c):
        self.colour = Colour
        if (a + b) > c and (b + c) > a and (a + c) > b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ExceptionTriangleNotExist("the triangle does not exist")

    def area(self):
        half_p = 0.5 * (self.c + self.a + self.b)
        square = (half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)) ** 0.5
        return square

    def perimeter(self):
        return self.a + self.b + self.c

    def showInformation(self):
        print('Triangle ', self.colour.showColour(self))


class Rectangle(Figure):
    def __init__(self, Colour, a, b):
        self.colour = Colour
        if a > 0 and b > 0:
            self.a = a
            self.b = b
        else:
            raise ExceptionSideisLessZero("side is less than zero")

    def area(self):
        return self.a * self.b

    def showInformation(self):
        print("Rectangle  ", self.colour.showColour(self))

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):
    def __init__(self, Colour, a):
        Rectangle.__init__(self, Colour, a, a)

    def showInformation(self):
        print("Square ", self.colour.showColour(self))
