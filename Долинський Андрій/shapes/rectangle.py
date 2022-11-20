from shape import Shape
from doesntExistException import doesntExistException
from colors import Color

class Rectangle(Shape):
    def __init__(self,Color, a, b):
        Shape.__init__(self,Color)
        if(a>0 and b>0):
            self.a = a
            self.b = b
        else:
            raise doesntExistException("Shape does not exist")


    def perimeter(self):
        perimeter = (self.a + self.b)*2
        return perimeter


    def area(self):
        area = self.a * self.b
        return area


    def print(self):
        print("Rectangle : ")
        Shape.print(self)