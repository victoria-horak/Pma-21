from dataclasses import dataclass


@dataclass
class Student:
    surname: ""
    name: ""
    dateOfBirth: ""
    gradesList: []

    def __str__(self):
        string = ""
        string += "Surname: " + self.surname + "\t"
        string += "Name: " + self.name + "\t"
        string += "Date of Birth: " + self.dateOfBirth + "\t"
        string += "Grades: "
        for i in self.gradesList:
            string += str(i) + " "
        return string
