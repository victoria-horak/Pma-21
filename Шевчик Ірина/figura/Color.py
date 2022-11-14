from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def get_color(self):
        pass


class Blue(Color):
    def get_color(self):
        return "Blue"


class Green(Color):
    def get_color(self):
        return "Green"


class Yellow(Color):
    def get_color(self):
        return "Yellow"
