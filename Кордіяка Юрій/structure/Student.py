from dataclasses import dataclass


@dataclass
class Student:
    last_name: str
    name: str
    date: str
    score: list

    def __str__(self):
        string = ""
        for i in self.score:
            if i != "":
                string += i + ' '
        l = self.last_name + ' ' + self.name + ' ' + self.date + ' ' + string
        return l
