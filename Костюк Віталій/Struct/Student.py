from dataclasses import dataclass


@dataclass
class Student:
    name: str
    last_name: str
    marks: list

    def __str__(self):
        marks_str = ""
        for mark in self.marks:
            marks_str += mark + ' '
        student_str = self.last_name + ' ' + self.name + ' ' + 'Marks:\n' + marks_str
        return student_str
