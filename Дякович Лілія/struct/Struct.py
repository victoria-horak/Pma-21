from dataclasses import dataclass


@dataclass
class Student:
    first_name: str
    second_name: str
    grades: list

    def __str__(self):
        string = ""
        string += self.first_name + " " + self.second_name + " "
        for i in self.grades:
            string += str(i) + " "
        return string
