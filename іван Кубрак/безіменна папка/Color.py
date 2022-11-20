from abc import ABC

class Color(ABC):

    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

class Blue(Color):
    def __init__(self):
        Color.__init__(self, "blue")        

class Yellow(Color):
     def __init__(self):
        Color.__init__(self, "yellow")
        
class Green(Color):
     def __init__(self):
        Color.__init__(self, "green")
        





    
