import datetime
from Exception import*


class Student:
    first_name: str
    last_name: str
    list_of_grades: list

    def __init__(self, data, name, surname, grades):
        if data[0] > 0 and data[1] > 0 and data[1] <= 12 and data[2] > 0:
            self.data = datetime.date(data[2],data[1],data[0])
        else:
            raise IncorrectData("Length is less than 0")
        self.first_name = name
        self.last_name = surname
        self.list_of_grades = grades

    def is_two(self):
        for i in range(len(self.list_of_grades)):
            if self.list_of_grades[i] == 2:
                return True
        return False

    def __str__(self):
        str1 = self.first_name+ ' '+ self.last_name+ ' ' +str(self.data)+ ' '
        for list_of_grades in (self.list_of_grades):
            str1 += str(list_of_grades) + ' '
        return str1
