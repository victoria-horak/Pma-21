from abc import ABC
from abc import abstractmethod


class Color(ABC):

    @abstractmethod
    def get_name_colour(self):
        pass
