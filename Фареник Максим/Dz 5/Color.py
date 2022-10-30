from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def __init__(self, color):
        pass

    @abstractmethod
    def getColor(self):
        pass


class Green(Color):
    def __init__(self):
        self.color = "green"

    def getColor(self):
        return self.color


class Blue(Color):
    def __init__(self):
        self.color = "blue"

    def getColor(self):
        return self.color


class Yellow(Color):
    def __init__(self):
        self.color = "yellow"

    def getColor(self):
        return self.color


class Red(Color):
    def __init__(self):
        self.color = "red"

    def getColor(self):
        return self.color
