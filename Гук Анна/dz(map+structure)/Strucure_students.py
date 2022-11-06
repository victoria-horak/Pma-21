from dataclasses import dataclass


@dataclass
class Student:
    surname: str
    name: str
    date_of_birth: str
    points: list

    def print(self):
        print("Surname:" + self.surname)
        print("Name:" + self.name)
        print("Date of birth:" + self.date_of_birth)
        print("All points:" + str(self.points))