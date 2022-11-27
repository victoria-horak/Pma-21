from Rectangle import Rectangle
from InvalidShapeException import InvalidShapeException
from Colors import Color

class Square(Rectangle):
    def __init__(self, color : Color, side):
        Rectangle.__init__(self, color, side, side)
