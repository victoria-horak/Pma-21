from dataclasses import dataclass
from datetime import date


@dataclass
class Student:
    surname: str
    name: str
    dataOfBirth: date
    grades: list

    def output(self):
        print("surname: ", self.surname)
        print("name: ", self.name)
        print("date of birth: ", self.dataOfBirth)
        print("grades", self.grades,'\n')
