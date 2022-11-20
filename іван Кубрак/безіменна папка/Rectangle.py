from classFigura import *
import turtle


class Rectangle(Figura):
     def __init__ (self, color: Color = Blue() , a=0 , b=0):
         self.color = color
         try:
             if  a < 0 or b < 0:
                    raise Exception

             self.a = a
             self.b = b

         except ValueError:
             print(" value error")
             
     def __str__(self):
        s = "Rectangle:" + '\n'
        s += "side 1: " + str(self.a) + " side 2: " + str(self.b) + '\n'
        s += "color: " + self.color.getColor() + '\n'
        s += "perimeter: " + str(self.perimeter()) + '\n'
        s += "area: " + str(self.area()) + '\n'
        return s

     def perimeter(self):
        return 2 * (self.a + self.b)

     def area(self):
        return self.a * self.b

     def paint(self):
        turtle.color(self.color.getColor())
        for i in range(2):
            turtle.forward(self.a)
            turtle.right(90)
            turtle.forward(self.b)
            turtle.right(90)
        time.sleep(3)
        turtle.Screen().reset()

    
        
        
            
             
            
         
