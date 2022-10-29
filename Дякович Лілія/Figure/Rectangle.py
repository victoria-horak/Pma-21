from Figure import Figure
from NotExistException import NotExistException


class Rectangle(Figure):
    def __init__(self,Color, a, b):
        Figure.__init__(self,Color)
        if(a>0 and b>0):
            self.a = a
            self.b = b
        else:
            raise NotExistException("Figure does not exist")


    def perum(self):
        perumetr = (self.a + self.b)*2
        return perumetr


    def square(self):
        space = self.a * self.b
        return space


    def print(self):
        print("Rectangle : ")
        Figure.print(self)
