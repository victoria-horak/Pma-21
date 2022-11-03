from Blue import Blue
from Figure import Figure


class Rectangle(Figure):
    def __init__(self, width=1, length=1, color=Blue()):
        if width < 0:
            raise ValueError("Width can`t be negative")
        if length < 0:
            raise ValueError("Length can`t be negative")

        self._width = width
        self._length = length
        self._color = color

    def perimeter(self):
        return 2 * (self._width * self._length)

    def area(self):
        return self._width * self._length

    def __str__(self):
        return f"""
Rectangle sizes: {self._length}x{self._width}
Color: {self._color.get_color()}
Perimeter: {self.perimeter()}
Area: {self.area()}"""
