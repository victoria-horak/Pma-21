from abc import abstractmethod, ABC


class Color(ABC):
    @abstractmethod
    def __init__(self, color):
        pass

    def printColor(self):
        pass


class Blue(Color):
    def __init__(self):
        self.color = 'Blue'

    def printColor(self, color='blue'):
        return color


class Green(Color):
    def __init__(self):
        self.color = 'Green'

    def printColor(self, color='green'):
        return color


class Yellow(Color):
    def __init__(self):
        self.color = 'Yellow'

    def printColor(self, color='yellow'):
        return color


class Pink(Color):
    def __init__(self):
        self.color = "Pink"

    def printColor(self, color='pink'):
        return color
