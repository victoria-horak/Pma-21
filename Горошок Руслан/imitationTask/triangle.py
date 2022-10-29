import math
from ShapeAbsClass.shape import Shape


class Triangle(Shape):

    def __init__(self, first_side, second_side, third_side, color):
        if first_side + second_side > third_side and first_side + third_side > first_side and second_side + \
                third_side > first_side:
            self.first_side = first_side
            self.second_side = second_side
            self.third_side = third_side
        else:
            self.first_side = 1
            self.second_side = 1
            self.third_side = 1
        self.color = color
        self.name = "Triangle"

    def get_perimeter(self):
        return self.first_side + self.second_side + self.third_side

    def get_area(self):
        half_perimeter = self.get_perimeter() / 2.0
        area = math.sqrt(half_perimeter * (half_perimeter - self.first_side) * (half_perimeter - self.second_side) * (
                half_perimeter - self.third_side))
        return round(area, 2)
