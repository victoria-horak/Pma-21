import datetime

from Struct import Student


def grade2(mass):
    new_mass = []
    for i in range(len(mass)):
        if isStudentHave2(mass[i]):
            new_mass.append(mass[i])
    return new_mass


def isStudentHave2(student):
    for i in student.grades:
        if i == 2:
            return True
    return False


def read(fileName=""):
    with open(fileName) as file:
        mass = []
        for row in file:
            temp = [x for x in row.split(" ")]
            first_name = temp[0]
            second_name = temp[1]
            data=datetime.date(int(temp[2]),int(temp[3]),int(temp[4]))
            grades = [int(x) for x in temp[5:len(temp)]]
            mass.append(Student(first_name, second_name, data, grades))
    return mass

