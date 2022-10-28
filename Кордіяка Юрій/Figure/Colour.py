from abc import abstractmethod, ABC


class Colour(ABC):
    @abstractmethod
    def showColour(self, colour):
        pass


class Blue(Colour):
    def __init__(self):
        self.colour = 'Blue'

    def showColour(self, colour='blue'):
        return colour


class Green(Colour):
    def __init__(self):
        self.colour = 'Green'

    def showColour(self, colour='green'):
        return colour


class Yellow(Colour):
    def __init__(self):
        self.colour = 'Yellow'

    def showColour(self, colour='yellow'):
        return colour
