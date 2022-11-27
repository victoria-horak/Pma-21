from Shape import Shape
from InvalidShapeException import InvalidShapeException
from Colors import Color

class Triangle(Shape):
    def __init__(self, color : Color, first_side, second_side, third_side):
        Shape.__init__(self, color, 'triangle')
        if not Triangle.check_triangle(first_side, second_side, third_side):
            raise InvalidShapeException('This shape is invalid')
        else:
            self.first_side = first_side
            self.second_side = second_side
            self.third_side = third_side
    @staticmethod
    def check_triangle(a, b, c):
        if c >= a + b or a >= b + c or b >= a + c or a <= 0 or b <= 0 or c <= 0:
            return False
        else:
            return True

    def get_perimeter(self):
        return self.first_side + self.second_side + self.third_side

    def get_square(self):
        p = self.get_perimeter() / 2
        result = (p * (p - self.first_side) * (p - self.second_side) * (p - self.third_side)) ** 0.5
        return result


