from dataclasses import dataclass
import datetime

@dataclass
class Student:
    firstName: str
    secondName: str
    dateOfBirthday: datetime.datetime(1,1,1)
    grades: [int]

    def __str__(self):
        string = f"{self.firstName} {self.secondName} \t"
        string += f"{self.dateOfBirthday}\t"
        string += "Grade: " + " ".join(str(i) for i in self.grades)
        return string

    def readFromString(self, string):
        arr = string.split(" ")
        self.firstName = arr[0]
        self.secondName = arr[1]
        self.dateOfBirthday = datetime.date(int(arr[2]),int(arr[3]),int(arr[4]))
        self.grades = [int(x) for x in arr[5:len(arr)]]
        return self
