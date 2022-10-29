from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass
