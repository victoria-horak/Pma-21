from Shape import Shape
from Checker import Checker
from InvalidShapeException import InvalidShapeException
from Colors import Color

class Rectangle(Shape):
    def __init__(self, color : Color, first_side, second_side):
        Shape.__init__(self, color, 'rectangle')
        if Checker.check_side(first_side) or Checker.check_side(second_side):
            raise InvalidShapeException('This shape is invalid')
        else:
            self.first_side = first_side
            self.second_side = second_side
    
    def get_perimeter(self):
        return 2 * (self.first_side + self.second_side)

    def get_square(self):
        return self.first_side * self.second_side