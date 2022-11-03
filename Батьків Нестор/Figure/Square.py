from Blue import Blue
from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, length=1, color=Blue()):
        if length < 0:
            raise ValueError("Length ca`t be negative")
        self._length = length
        self._color = color

    def area(self):
        return self._length * self._length

    def perimeter(self):
        return self._length * 4

    def __str__(self):
        return f"""
Square length: {self._length}
Color: {self._color.get_color()}
Perimeter: {self.perimeter()}
Area: {self.area()}"""
