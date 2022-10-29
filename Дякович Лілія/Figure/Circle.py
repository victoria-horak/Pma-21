from Figure import Figure
from NotExistException import NotExistException

class Circle(Figure):
    def __init__(self, Color, r):
        Figure.__init__(self, Color)
        if(r>0):
            self.r = r
        else:
            raise NotExistException("Circle does not exist")

    def perum(self):
        return 2 * self.r * 3.14

    def square(self):
        return round((3.14 * self.r * self.r), 2)

    def print(self):
        print("Circle :")
        Figure.print(self)
