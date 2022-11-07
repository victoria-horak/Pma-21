from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    def printColor(self):
        return self.color.getColor()

    def getArea(self):
        pass

    def getPerimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        super().__init__(color)

    def getArea(self):
        return math.pi * self.radius ** 2

    def getPerimeter(self):
        return 2 * math.pi* self.radius

class Triangle(Shape):
    def __init__(self, a, b, c, color):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(color)

    def getArea(self):
        s = self.getPerimeter() / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

    def getPerimeter(self):
        return self.a + self.b + self.c

class Rectangle(Shape):
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        super().__init__(color)

    def getArea(self):
        return self.a * self.b

    def getPerimeter(self):
        return 2 * (self.a + self.b)

class Square(Rectangle):
    def __init__(self, a, color):
        super().__init__(a, a, color)

class Color(ABC):
    @abstractmethod
    def getColor(self):
        pass

class Blue(Color):
    def getColor(self):
        return "blue"

class Green(Color):
    def getColor(self):
        return "green"

class Yellow(Color):
    def getColor(self):
        return "yellow"



blue = Blue()
green = Green()
yellow = Yellow()

blueCircle = Circle(3, blue)
yellowTriangle = Triangle(6, 6, 6, yellow)
greenSquare = Square(5, green)
blueRectangle = Rectangle(4, 5, blue)

print("Circle :")
print("Area =", blueCircle.getArea())
print("Perimeter =", blueCircle.getPerimeter())
print("Color =", blueCircle.printColor())

print("\nTriangle :")
print("Area =", yellowTriangle.getArea())
print("Perimeter =", yellowTriangle.getPerimeter())
print("Color =", yellowTriangle.printColor())

print("\nSquare :")
print("Area =", greenSquare.getArea())
print("Perimeter =", greenSquare.getPerimeter())
print("Color =", greenSquare.printColor())

print("\nRectangle :")
print("Area =", blueRectangle.getArea())
print("Perimeter =", blueRectangle.getPerimeter())
print("Color =", blueRectangle.printColor())
