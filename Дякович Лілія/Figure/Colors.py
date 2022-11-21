from abc import abstractmethod, ABC


class Color(ABC):
    @abstractmethod
    def __init__(self, color):
        pass

    def printColor(self):
        pass





