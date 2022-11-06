from abc import ABC, abstractmethod
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
