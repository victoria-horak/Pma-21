from ColorAbsClass.color import Color


class Blue(Color):

    def __init__(self):
        self.colour_name = "Blue"

    def get_name_colour(self):
        return self.colour_name
