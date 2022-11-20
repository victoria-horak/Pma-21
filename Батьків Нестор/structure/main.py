from Student import Student
import datetime
import re


def input_from_file(filename):
    with open(filename) as file:

        students = []
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            line = line.split(" ")
            grades = []
            for index in range(3, len(line)):
                grades.append(int(line[index]))
            date = datetime.date(*reversed([int(elem) for elem in line[2].split(".") ]))
            student = Student(line[0],line[1], date, grades)
            students.append(student)
        return students


students = input_from_file("students.txt")
print("\tSurname\tName\tDate\tGrades")
for student in students:
    print(student, "\n")

students_with_2 = [student for student in students if 2 in student.grades]
students_with_2.sort(key=lambda student: student.surname)
print("sorted by surname with mark 2:")
for student in students_with_2:
    print(student, "\n")
if len(students_with_2) == 0:
    print("No students found")