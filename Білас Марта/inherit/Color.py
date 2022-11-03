from abc import ABC


class Color(ABC):
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color


class Green(Color):
    def __init__(self):
        Color.__init__(self, "green")


class Blue(Color):
    def __init__(self):
        Color.__init__(self, "blue")


class Purple(Color):
    def __init__(self):
        Color.__init__(self, "purple")
