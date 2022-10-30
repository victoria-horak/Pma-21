class Color:
    @staticmethod
    def getColor():
        pass


class Green(Color):
    color = "Green"

    @staticmethod
    def getColor():
        return Green.color


class Blue(Color):
    color = "Blue"

    @staticmethod
    def getColor():
        return Blue.color


class Yellow(Color):
    color = "Yellow"

    @staticmethod
    def getColor():
        return Yellow.color
