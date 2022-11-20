from Figure import *


class Circle(Figure):

    def __init__(self, color: Color = Blue(), radius=0):
        try:
            if radius < 0:
                raise WrongParameters
            self.radius = radius
        except ValueError:
            print(" value error")
        except WrongParameters:
            print("wrong parameters")
        self.color = color

    def __str__(self):
        result = "Circle:" + '\n'
        result += "radius : " + str(self.radius) + '\n'
        result += "color: " + self.color.getColor() + '\n'
        result += "perimeter: " + str(self.perimeter()) + '\n'
        result += "area: " + str(self.area()) + '\n'
        return result

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def draw(self):
        turtle.color(self.color.getColor())
        turtle.circle(self.radius)
        time.sleep(3)
        turtle.Screen().reset()
