from ShapeAbsClass.shape import Shape


class Quadrangle(Shape):

    def __init__(self, side, color):
        if side > 0:
            self.side = side
        else:
            self.side = 1
        self.color = color
        self.name = "Quadrangle"

    def get_perimeter(self):
        return 4 * self.side

    def get_area(self):
        return self.side ** 2
