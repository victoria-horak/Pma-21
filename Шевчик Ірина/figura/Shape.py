from abc import ABC, abstractmethod
from Color import Color
import math


class Shape(ABC):
    def __init__(self, color: Color):
        self.__color = color

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def show(self):
        pass

    def get_color(self):
        return self.__color.get_color()


class Triangle(Shape):
    def __init__(self, side_a: int, side_b: int, side_c: int, color: Color):
        super().__init__(color)
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def calculate_area(self):
        half_perimeter = self.calculate_perimeter() / 2
        return math.sqrt(half_perimeter * (half_perimeter - self.__side_a)
                         * (half_perimeter - self.__side_b)
                         * (half_perimeter - self.__side_c))

    def calculate_perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

    def show(self):
        print(
            f"Triangle\n\tColor: {self.get_color()}\n\tArea: {self.calculate_area()}\n\tPerimeter: {self.calculate_perimeter()}")


class Circle(Shape):
    def __init__(self, color: Color, radius: int):
        super().__init__(color)
        self.__radius = radius

    def calculate_area(self):
        return math.pi * (self.__radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

    def show(self):
        print(
            f"Circle\n\tColor: {self.get_color()}\n\tArea: {self.calculate_area()}\n\tPerimeter: {self.calculate_perimeter()}")


class Square(Shape):
    def __init__(self, color: Color, side: int):
        super().__init__(color)
        self.__side = side

    def calculate_area(self):
        return self.__side ** 2

    def calculate_perimeter(self):
        return self.__side * 4

    def show(self):
        print(
            f"Square\n\tColor: {self.get_color()}\n\tArea: {self.calculate_area()}\n\tPerimeter: {self.calculate_perimeter()}")


class Rectangle(Shape):
    def __init__(self, side_a: int, side_b: int, color: Color):
        super().__init__(color)
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return self.__side_a * self.__side_b

    def calculate_perimeter(self):
        return 2 * (self.__side_a + self.__side_b)

    def show(self):
        print(
            f"Rectangle\n\tColor: {self.get_color()}\n\tArea: {self.calculate_area()}\n\tPerimeter: {self.calculate_perimeter()}")
