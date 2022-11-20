from classFigura import *
import turtle

class Circle(Figura):
    def __init__ (self, color: Color = Yellow() , r=0 ):
        self.color = color
        try:
            if r<0 :
                raise Exception

            self.radius = r

        except ValueError:
            print(" value error")

    def __str__(self):
    
        s = "Circle:" + '\n'
        s += "radius : " + str(self.radius) + '\n'
        s += "color: " + self.color.getColor() + '\n'
        s += "perimeter: " + str(self.perimeter()) + '\n'
        s += "area: " + str(self.area()) + '\n'
        return s

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def paint (self):
        turtle.color(self.color.getColor())
        turtle.circle(self.radius)
        time.sleep(3)
        turtle.Screen().reset()

    


    
