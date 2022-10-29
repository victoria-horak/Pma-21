from ShapeAbsClass.shape import Shape


class Circle(Shape):
    Pi = 3.14

    def __init__(self, radius, color):
        if radius > 0:
            self.radius = radius
        else:
            self.radius = 1
        self.color = color
        self.name = "Circle"

    def get_perimeter(self):
        return 2 * Circle.Pi * self.radius

    def get_area(self):
        return Circle.Pi * self.radius ** 2
