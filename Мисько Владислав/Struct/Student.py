from typing import NamedTuple

class Student(NamedTuple):
    surname: str
    name: str
    date_of_birth: str
    marks: list

    def print(self):
        print('Surname: ' + self.surname)
        print('Name: ' + self.name)
        print('Date of birth: ' + self.date_of_birth)
        print('Marks: ' + str(self.marks))
        print('---------------------------')