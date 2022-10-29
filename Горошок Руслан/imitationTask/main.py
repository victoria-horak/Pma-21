from TriangleClass.triangle import Triangle
from QuadrangleClass.quadrangle import Quadrangle
from RectangleClass.rectangle import Rectangle
from CircleClass.circle import Circle


from GreenColorClass.green import Green
from BlueColorClass.blue import Blue
from YellowColorClass.yellow import Yellow


def print_info(obj):
    print("Shape name :", obj.name)
    print("Perimetr = ", obj.get_perimeter())
    print("Area = ", obj.get_area())
    print("Colour this shape is", obj.color.get_name_colour())
    print("\n")


triangle_color = Green()
quadrangle_color = Yellow()
rectangle_color = Blue()
circle_color = Green()

triangle = Triangle(3, 4, 5, triangle_color)
print_info(triangle)

rectangle = Rectangle(4, 2, rectangle_color)
print_info(rectangle)

quadrangle = Quadrangle(-5, quadrangle_color)
print_info(quadrangle)

circle = Circle(-4, circle_color)
print_info(circle)
