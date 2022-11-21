from dataclasses import dataclass
import datetime


@dataclass
class Student:
    first_name: str
    second_name: str
    data: datetime.datetime(1, 1, 1)
    grades: list

    def __str__(self):
        string = ""
        string += self.first_name + " " + self.second_name + "   "
        string += str(self.data)+"   "
        for i in self.grades:
            string += str(i) + " "
        return string
