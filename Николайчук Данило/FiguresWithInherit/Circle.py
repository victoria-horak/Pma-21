from Figurs import *


class Circle(Figur):

    def __init__(self, color: Color = Black(), radius=1):
        Figur.__init__(self, color)
        if radius < 0:
            raise DifferentError("radius of circle is less then zero.")
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def square(self):
        return 3.14 * self.radius ** 2

    def __str__(self):
        return f"Circle:\ncolor = {self.color.getColor()}\nradius = {self.radius}\nperimeter = {self.perimeter()}\nsquare = {self.square()}\n"

    def draw(self):
        turtle.fillcolor(self.color.getColor())
        turtle.begin_fill()
        turtle.circle(self.radius * 15)
        turtle.end_fill()
        time.sleep(7)
        turtle.Screen().reset()
