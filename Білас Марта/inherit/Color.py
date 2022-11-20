from abc import ABC


class Color(ABC):
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
