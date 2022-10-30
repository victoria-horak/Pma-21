from abc import ABC, abstractmethod
from Colors import *

class Shape(ABC):
    def __init__(self, color : Color, name):
        self.color = color
        self.name = name
    
    @abstractmethod
    def get_perimeter(self):
        pass
    @abstractmethod
    def get_square(self):
        pass

    def print_info(self):
        print('Name - ', self.name)
        print('S = ', self.get_square())
        print('P = ', self.get_perimeter())
        print('Color - ', self.color.get())
        print()