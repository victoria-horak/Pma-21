from dataclasses import dataclass

@dataclass

class Student:
    
    name: str
    surname : str
    data_birth : str
    marks : list
    average : int

    def student_print(self):
        print("name:" , self.name)
        print("surname:", self.surname)
        print("data_birth:", self.data_birth)
        print("marks:", self.marks)
        print("average mark:", self.average,"\n")

    def Dviyochnuku_print(self):
        print( self.name, self.surname)

    def average_mark (self):
        self.average = sum(self.marks)/len(self.marks)

    
    
