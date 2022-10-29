from abc import abstractmethod,ABC
from bridge import Colour
from error import Error

class Shape(ABC):
    @abstractmethod
    def __init__(self,Colour):
        self.colour=Colour

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def print(self):
        print("The perimeter of the shape:",self.perimetr(),"\n","The area of the shape:",self.area(),"\n","The colour of the shape:",self.colour.print_colour(self),"\n")




class Rectangle(Shape):

    def __init__(self,first_side, second_side, Colour):

        Shape.__init__(self, Colour)
        if first_side>0 and second_side>0:
            self.first_side=first_side
            self.second_side = second_side
        else:
            raise Error("!!The value of first and second side should be bigger!!")

    def perimetr(self):

        perim=2*(self.first_side+self.second_side)
        return perim

    def area(self):
        area=self.first_side*self.second_side
        return area

    def print(self):
        print("--RECTANGLE--")
        Shape.print(self)


class Triangle(Shape):

    def __init__(self, first_side, second_side, third_side, Colour):

        Shape.__init__(self, Colour)
        if first_side > 0 and second_side > 0 and (first_side+second_side)>third_side and (first_side+third_side)>second_side and (third_side+second_side)>first_side:
            self.first_side = first_side
            self.second_side = second_side
            self.third_side = third_side
        else:
            raise Error("!!The value of first,second and third side should be bigger!!")

    def perimetr(self):

        perim = self.first_side + self.second_side + self.third_side
        return perim

    def area(self):
        half_perimetr=Triangle.perimetr(self)/2
        area = ((half_perimetr*(half_perimetr-self.first_side)*(half_perimetr-self.second_side)*(half_perimetr-self.third_side))**0.5)
        return area

    def print(self):
        print("--TRIANGLE--")
        Shape.print(self)


class Square(Shape):

    def __init__(self, side, Colour):

        Shape.__init__(self, Colour)
        if side > 0:
            self.side = side

        else:
            raise Error("!!The value of first and second side should be bigger!!")

    def perimetr(self):

        perim = 4*self.side
        return perim

    def area(self):
        area = self.side**2
        return area

    def print(self):
        print("--SQUARE--")
        Shape.print(self)


class Circle(Shape):

    def __init__(self, radius, Colour):

        Shape.__init__(self, Colour)
        if radius > 0 :
            self.radius = radius

        else:
            raise Error("!!The value of first and second side should be bigger!!")

    def perimetr(self):

        circuit = 2 * self.radius * 3.14
        return circuit

    def area(self):
        area = 3.14*(self.radius**2)
        return area

    def print(self):
        print("--CIRCLE--")
        Shape.print(self)
