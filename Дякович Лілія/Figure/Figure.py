from abc import ABC, abstractmethod, ABC
from Colors import Color


class Figure(ABC):
    @abstractmethod
    def __init__(self, Color):
        self.color = Color

    @abstractmethod
    def perum(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def print(self):
        print("perumetr = ", self.perum(), "  square = ", self.square(), "  color = ", self.color.printColor(self),"\n")
