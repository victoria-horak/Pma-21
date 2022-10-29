from QuadrangleClass.quadrangle import Quadrangle


class Rectangle(Quadrangle):

    def __init__(self, side, second_side, color):
        super().__init__(side, color)
        if second_side > 0 and side > 0:
            self.second_side = second_side
        else:
            self.second_side = 1
        self.name = "Rectangle"

    def get_perimeter(self):
        return (self.side + self.second_side) * 2

    def get_area(self):
        return self.side * self.second_side
