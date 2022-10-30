class Colour:
    @staticmethod
    def getColour():
        pass


class Yellow(Colour):
    colour = "Yellow"

    @staticmethod
    def getColour():
        return Yellow.colour


class Green(Colour):
    colour = "Green"

    @staticmethod
    def getColour():
        return Green.colour


class Blue(Colour):
    colour = "Blue"

    @staticmethod
    def getColour():
        return Blue.colour
