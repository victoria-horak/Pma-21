from Shape import Shape
from InvalidShapeException import InvalidShapeException
from Colors import Color


class Circle(Shape):
    def __init__(self, color: Color, radius):
        Shape.__init__(self, color, 'circle')
        if radius <= 0:
            raise InvalidShapeException('This shape is invalid')
        else:
            self.radius = radius

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def get_square(self):
        return 3.14 * self.radius * self.radius

