from abc import ABC, abstractmethod
from Color import *


class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def changeColor(self, color):
        try:
            if color != "green" or color != "purple" or color != "blue":
                raise ValueError
            self.color = Color(color)
        except ValueError:
            print("there is not such color")

