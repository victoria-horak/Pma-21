from Shape import Shape
from InvalidShapeException import InvalidShapeException
from Colors import Color


class Rectangle(Shape):
    def __init__(self, color: Color, first_side, second_side):
        Shape.__init__(self, color, 'rectangle')
        if first_side <= 0 or second_side <= 0:
            raise InvalidShapeException('This shape is invalid')
        else:
            self.first_side = first_side
            self.second_side = second_side

    def get_perimeter(self):
        return 2 * (self.first_side + self.second_side)

    def get_square(self):
        return self.first_side * self.second_side
