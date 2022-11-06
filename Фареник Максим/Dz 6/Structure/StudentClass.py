from dataclasses import dataclass


@dataclass
class Student:
    firstName: str
    lastName: str
    birthday: str
    marks: list

    def __str__(self):
        printMarks = ""
        for iterator in self.marks:
            printMarks += iterator + ','
        student = self.firstName + ' ' + self.lastName + ' ' + self.birthday + ' Marks: ' + printMarks[:-1]
        return student
