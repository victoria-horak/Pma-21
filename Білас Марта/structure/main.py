from Student import *


def outputFromFile(allStudents):
    with open("data.txt") as file:
        try:
            for line in file:
                if not line.isspace():
                    line = line.split(", ")
                    if line.__len__() == 4:
                        grades = []
                        for grade in line[3].split(" "):
                            grades.append(int(grade))
                        student = Student(line[0], line[1], line[2], grades)
                        allStudents.append(student)
        except ValueError:
            print("wrong element type")


allStudents = []
outputFromFile(allStudents)
print("all students: ")
for element in allStudents:
    element.output()
allStudents.sort(key=lambda student: student.surname)
studentsWithMark2 = [student for student in allStudents if 2 in student.grades]
print("students with mark 2: ")
if studentsWithMark2.__len__() != 0:
    for element in studentsWithMark2:
        element.output()
else:
    print("there is no student with mark 2")
