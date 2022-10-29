from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, Color, a):
        Rectangle.__init__(self, Color, a, a)

    def square(self):
        return self.a * self.a

    def perum(self):
        return self.a * 4

    def print(self):
        print("Square :\nperumetr = ", self.perum(), "  square = ", self.square(), "  color = ",
              self.color.printColor(self), "\n")
