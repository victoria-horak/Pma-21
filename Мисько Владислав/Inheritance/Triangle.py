from Shape import Shape
from Checker import Checker
from InvalidShapeException import InvalidShapeException
from Colors import Color

class Triangle(Shape):
    def __init__(self, color : Color, first_side, second_side, third_side):
        Shape.__init__(self, color, 'triangle')
        if not Checker.check_sides_of_triangle(first_side, second_side, third_side):
            raise InvalidShapeException('This shape is invalid')
        else:
            self.first_side = first_side
            self.second_side = second_side
            self.third_side = third_side
    
    def get_perimeter(self):
        return self.first_side + self.second_side + self.third_side

    def get_square(self):
        p = self.get_perimeter() / 2
        result = (p * (p - self.first_side) * (p - self.second_side) * (p - self.third_side)) ** 0.5
        return result

