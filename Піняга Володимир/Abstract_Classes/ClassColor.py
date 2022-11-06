from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def __init__(self, color):
        pass

    def print_color(self):
        pass


class Blue(Color):
    def __init__(self):
        self.color = color

    def print_color(self, color='Blue'):
        return color


class Green(Color):
    def __init__(self):
        self.color = color

    def print_color(self, color='Green'):
        return color


class Yellow(Color):
    def __init__(self):
        self.color = color

    def print_color(self, color='Yellow'):
        return color
