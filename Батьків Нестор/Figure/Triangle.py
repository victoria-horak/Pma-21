from Blue import Blue
from Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a=1, side_b=1, side_c=1, color=Blue()):
        if side_a + side_b <= side_c or side_b + side_c <= side_a or side_a + side_c <= side_b:
            raise ValueError("Triangle with such sides does not exist")
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c
        self._color = color

    def perimeter(self):
        return self._side_a + self._side_b + self._side_c

    def area(self):
        half_p = self.perimeter() / 2
        return round((half_p * (half_p - self._side_a)*(half_p - self._side_b)*(half_p - self._side_c))**0.5, 2)

    def __str__(self):
        return f"""
Triangle sides: {self._side_a},{self._side_b},{self._side_c}
Color: {self._color.get_color()}
Perimeter: {self.perimeter()}
Area: {self.area()}"""
