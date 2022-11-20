from Rectangle import *
import turtle


class Square(Rectangle):
     def __init__ (self, color: Color = Blue() , a=0 ):
      
         Rectangle.__init__(self,color , a , a )
         try:
             if  a < 0 :
                    raise Exception

             self.a = a

         except ValueError:
             print(" value error")
         self.color = color
     
     def __str__(self):
        s = "Square:" + '\n'
        s += "side : " + str(self.a) + '\n'
        s += "color: " + str(self.color.getColor()) + '\n'
        s += "perimeter: " + str(self.perimeter()) + '\n'
        s += "area: " + str(self.area()) + '\n'
        return s

     def perimeter(self):
        return 2 * (self.a + self.b)

     def area(self):
        return self.a * self.b
   

    
