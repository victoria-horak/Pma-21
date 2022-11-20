from shape import Shape
from doesntExistException import doesntExistException
from colors import Color

class Circle(Shape):
    def __init__(self, Color, r):
        Shape.__init__(self, Color)
        if(r>0):
            self.r = r
        else:
            raise doesntExistException("Circle does not exist")

    def perimeter(self):
        return 2 * self.r * 3.14

    def area(self):
        return round((3.14 * self.r * self.r), 2)

    def print(self):
        print("Circle :")
        Shape.print(self)