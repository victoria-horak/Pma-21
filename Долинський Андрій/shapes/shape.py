from abc import ABC, abstractmethod, ABC
from colors import Color


class Shape(ABC):
    @abstractmethod
    def __init__(self, Color):
        self.color = Color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def print(self):
        print("perimeter = ", self.perimeter(), "  area = ", self.area(), "  color = ", self.color.printColor(self),"\n")