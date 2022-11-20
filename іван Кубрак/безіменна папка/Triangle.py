
from math import *
from classFigura import *
import turtle

class Triangle(Figura):

    def __init__(self, color: Color = Blue(), a=0, b=0, c=0):
      try:
            if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
                raise Exception
            self.a = a
            self.b = b
            self.c = c
      
      except ValueError:
             print(" value error")
      self.color = color

    def __str__(self):
        s = "Triangle:" + '\n'
        s += "side 1: " + str(self.a) + " side 2: " + str(self.b) + " side 3: " + str(
            self.c) + '\n'
        s += "color: " + self.color.getColor() + '\n'
        s += "perimeter: " + str(self.perimeter()) + '\n'
        s += "area: " + str(self.area()) + '\n'
        return s

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)) 
        return s

    def angle(self, a, b, c):
        return degrees(acos((b ** 2 + c ** 2 - a ** 2) / (
                2.0 * b * c)))

    def canDraw (self):
        return self.a + self.b > self.c and self.b + self.c > self.a \
               and self.c + self.a > self.b

    def paint(self):
        turtle.color(self.color.getColor())
        if self.a == self.b == self.c:
            for i in range(3):
                turtle.forward(self.a)
                turtle.left(120)
        elif not self.canDraw():
            print("this triangle can't be drawn")
        else:
            turtle.forward(self.c)
            turtle.left(180 - self.angle(self.b, self.c, self.a))
            turtle.forward(self.a)
            turtle.left(180 - self.angle(self.c, self.a, self.b))
            turtle.forward(self.b)
        time.sleep(3)
        turtle.Screen().reset()
