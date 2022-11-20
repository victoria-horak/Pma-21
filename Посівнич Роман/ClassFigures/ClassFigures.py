from Invalid import Invalid
from abc import ABC, abstractmethod
from math import sqrt, pi


class ColorBase(ABC):
    @abstractmethod
    def getColor(self):
        pass


class Blue(ColorBase):
    def getColor(self):
        return 'Blue'


class Green(ColorBase):
    def getColor(self):
        return 'Green'


class Orange(ColorBase):
    def getColor(self):
        return 'Orange'


class Yellow(ColorBase):
    def getColor(self):
        return 'Yellow'


class ShapeBase(ABC):
    @abstractmethod
    def __init__(self, color: ColorBase):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def getColor(self):
        return self.color.getColor()


class Triangle(ShapeBase):
    def __init__(self, a, b, c, color: ColorBase):
        super().__init__(color)
        self.a = a
        if a <= 0:
            raise Invalid("Incorrect value")
        self.b = b
        if b <= 0:
            raise Invalid("Incorrect value")
        self.c = c
        if c <= 0:
            raise Invalid("Incorrect value")
        if a + b < c and a + c < b and b + c < a:
            raise Invalid("Incorrect value")

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a)*(s - self.b)*(s - self.c))


class Circle(ShapeBase):
    def __init__(self, r, color: ColorBase):
        super().__init__(color)
        self.r = r
        if r <= 0:
            raise Invalid("Incorrect value")

    def perimeter(self):
        return self.r * 2 * pi

    def area(self):
        return self.r * self.r * pi


class Rectangle(ShapeBase):
    def __init__(self, a, b, color: ColorBase):
        super().__init__(color)
        self.a = a
        if a <= 0:
            raise Invalid("Incorrect value")
        self.b = b
        if b <= 0:
            raise Invalid("Incorrect value")

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a, color: ColorBase):
        super().__init__(a, a, color)

