from dataclasses import dataclass


@dataclass
class Student:
    surname: ""
    name: ""
    dateOfBirth: ""
    gradesList: []

    def __str__(self):
        string = ""
        string += "Surname: {} Name: {} Date of Birth: {} Grades: {} ".format(self.surname, self.name, self.dateOfBirth,
                                                                              self.gradesList)
        return string
