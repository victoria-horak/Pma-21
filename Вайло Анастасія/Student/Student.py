from typing import NamedTuple
from datetime import datetime

class Student(NamedTuple):
    surname: str
    name: str
    date_of_birth: datetime.date
    marks: list

    def print(self):
        print('surname: ' + self.surname)
        print('name: ' + self.name)
        print('was born on: '  + self.date_of_birth.strftime('%d.%m.%Y'))
        print('marks: ' + str(self.marks))
