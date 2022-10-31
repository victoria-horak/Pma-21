from Figurs import *


class Rectangle(Figur):
    def __init__(self, color: Color = Black(), width=1, length=1):
        Figur.__init__(self, color)
        if width < 0 or length < 0:
            raise DifferentError("the length of the sides is unsatisfactory.")
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def square(self):
        return self.width * self.width

    def __str__(self):
        return f"Rectangle:\ncolor = {self.color.getColor()}\nwidth = {self.width}\nlength = {self.length}" \
               f"\nperimeter = {self.perimeter()}\nsquare = {self.square()}\n"

    def draw(self):
        turtle.fillcolor(self.color.getColor())
        begin_fill()
        for i in range(2):
            forward(self.length * 15)
            right(90)
            forward(self.width * 15)
            right(90)
        end_fill()
        time.sleep(7)
        turtle.Screen().reset()
