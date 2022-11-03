from Figure import Figure
from Blue import Blue
from math import pi


class Circle(Figure):
    def __init__(self, radius=0, color=Blue()):
        if radius < 0:
            raise ValueError("Radius can`t be negative")
        self._color = color
        self._radius = radius

    def area(self):
        return round(pi * self._radius*self._radius, 1)

    def perimeter(self):
        return round(2 * pi * self._radius, 1)

    def __str__(self):
        return f"""
Circle radius: {self._radius} 
Color: {self._color.get_color()}
Length: {self.perimeter()}
Area: {self.area()}
        """
