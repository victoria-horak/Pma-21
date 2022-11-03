from abc import ABC
from abc import abstractmethod


class Figure(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
