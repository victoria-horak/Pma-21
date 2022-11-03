from abc import ABC


class Color(ABC):
    def __init__(self):
        pass

    def get_color(self):
        return self._color
