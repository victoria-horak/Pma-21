from dataclasses import dataclass


@dataclass
class Student:
    firstName: str
    secondName: str
    dateOfBirthday: [int]
    grades: [int]

    def __str__(self):
        string = f"{self.firstName} {self.secondName} \t"
        string += f"{self.dateOfBirthday[0]}/{self.dateOfBirthday[1]}/{self.dateOfBirthday[2]}\t"
        string += "Grade: " + " ".join(str(i) for i in self.grades)
        return string

    def readFromString(self, string):
        arr = string.split(" ")
        self.firstName = arr[0]
        self.secondName = arr[1]
        self.dateOfBirthday = [int(x) for x in arr[2:5]]
        self.grades = [int(x) for x in arr[5:len(arr)]]
        return self
