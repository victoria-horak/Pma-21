from typing import NamedTuple


class Student(NamedTuple):
    Surname: str
    Name: str
    dateOfBirthday: int
    marks: list

    def __str__(self):
        return "Surname: " + self.Surname + "\tName: " + self.Name + "\tDate of birthday: " + str(
            self.dateOfBirthday) + "\tMarks: " + str(self.marks)
