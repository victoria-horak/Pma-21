from Rectangle import *


class Square(Rectangle):
    def __init__(self, color: Color = Black(), side=1):
        Rectangle.__init__(self, color, side, side)

    def __str__(self):
        return f"Square:\ncolor = {self.color.getColor()}\nside:{self.width}\nperimeter = {self.perimeter()}\nsquare = {self.square()}\n"
