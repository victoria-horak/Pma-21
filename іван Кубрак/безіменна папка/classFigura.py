from abc import ABC, abstractmethod
from Color import *
import time

class Figura(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def paint(self):
        pass

    def changeColor(self, color):
        try:
            if color != "green" or color != "purple" or color != "blue":
                raise ValueError
            self.color = Color(color)
        except ValueError:
            print("нема такого кольору")
