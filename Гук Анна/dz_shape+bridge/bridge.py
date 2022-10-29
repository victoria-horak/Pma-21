from abc import abstractmethod,ABC

class Colour(ABC):
    @abstractmethod
    def __init__(self,colour):
        pass

    def print_colour(self):
        pass


class Green(Colour):
    def __init__(self):
        self.colour="GREEN"

    def print_colour(self,colour="GREEN"):
        return colour


class Purple(Colour):
    def __init__(self):
        self.colour = "PURPLE"

    def print_colour(self, colour="PURPLE"):
        return colour


class Orange(Colour):
    def __init__(self):
        self.colour = "ORANGE"

    def print_colour(self, colour="ORANGE"):
        return colour


class Blue(Colour):
    def __init__(self):
        self.colour = "BLUE"

    def print_colour(self, colour="BLUE"):
        return colour

class Yellow(Colour):
    def __init__(self):
        self.colour = "YELLOW"

    def print_colour(self, colour="YELLOW"):
        return colour

class Red(Colour):
    def __init__(self):
        self.colour = "RED"

    def print_colour(self, colour="RED"):
        return colour