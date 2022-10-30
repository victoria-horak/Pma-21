from abc import ABC, abstractmethod
import math
from InvalidSizes import InvalidSizes
from ClassColor import Color


class Shape(ABC):
    @abstractmethod
    def __init__(self, Color):
        self.color = Color

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, first, second, third, Color):
        Shape.__init__(self, Color)
        if (first + second > third and
                first + third > second and
                second + third > first):
            self.first = first
            self.second = second
            self.third = third
        else:
            raise InvalidSizes("The dimensions entered for Triangle are invalid!")

    def square(self):
        p = (self.first + self.second + self.third) / 2
        return math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third))

    def perimeter(self):
        return self.first + self.second + self.third

    def show(self):
        print("Triangle: a = %d, b = %d, c = %d" % (self.first, self.second, self.third))
        print("Color of triangle: ", self.color)
        print("Square = ", self.square())
        print("Perimeter = ", self.perimeter())


class Circle(Shape):
    def __init__(self, radius, Color):
        Shape.__init__(self, Color)
        if radius > 0:
            self.radius = radius
        else:
            raise InvalidSizes("The dimensions entered for Circle are invalid!")

    def square(self):
        return math.pi * pow(self.radius, 2)

    def perimeter(self):  # length of circle
        return 2 * math.pi * self.radius

    def show(self):
        print("Circle: R = %d" % self.radius)
        print("Color of circle: ", self.color)
        print("Square = ", self.square())
        print("Perimeter = ", self.perimeter())


class Rectangle(Shape):
    def __init__(self, first, second, Color):
        Shape.__init__(self, Color)
        if first > 0 and second > 0:
            self.first = first
            self.second = second
        else:
            raise InvalidSizes("The dimensions entered for Rectangle are invalid!")

    def square(self):
        return self.first * self.second

    def perimeter(self):
        return (self.first + self.second) * 2

    def show(self):
        print("Rectangle: a = %d, b = %d" % (self.first, self.second))
        print("Color of Rectangle: ", self.color)
        print("Square = ", self.square())
        print("Perimeter = ", self.perimeter())


class Square(Rectangle):
    def __init__(self, first):
        Rectangle.__init__(self, first, first, Color)

    def show(self):
        print("Square: a = %d" % self.first)
        print("Color of square: ", self.color)
        print("Square = ", self.square())
        print("Perimeter = ", self.perimeter())

