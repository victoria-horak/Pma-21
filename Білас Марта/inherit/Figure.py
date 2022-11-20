from abc import ABC, abstractmethod
from Green import *
from Blue import *
from Purple import *
from Exception import *
import time
import turtle


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
        self.color.setColor(color)
