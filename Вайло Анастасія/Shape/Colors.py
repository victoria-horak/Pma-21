from abc import ABC

class Color(ABC):
    def __init__(self, color):
        self.color = color
    def get(self):
        pass

class Red(Color):
    def __init__(self):
        Color.__init__('Red')
    def get():
        return 'Red'

class Blue(Color):
    def __init__(self):
        Color.__init__('Blue')
    def get():
        return 'Blue'

class Yellow(Color):
    def __init__(self):
        Color.__init__('Yellow')
    def get():
        return 'Yellow'

class Green(Color):
    def __init__(self):
        Color.__init__('Green')
    def get():
        return 'Green'

