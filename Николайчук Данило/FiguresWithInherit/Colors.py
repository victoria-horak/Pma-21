from abc import ABC


class Color(ABC):
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color


class Red(Color):
    def __init__(self):
        Color.__init__(self, "red")


class Black(Color):
    def __init__(self):
        Color.__init__(self, "black")


class Green(Color):
    def __init__(self):
        Color.__init__(self, "green")


class Yellow(Color):
    def __init__(self):
        Color.__init__(self, "yellow")


class Blue(Color):
    def __init__(self):
        Color.__init__(self, "blue")
