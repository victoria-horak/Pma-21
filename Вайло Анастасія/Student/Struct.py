from Student import *
from datetime import datetime


def encrypt_data(thelist):
    result = []
    current_number = 0

    thelist = thelist.strip(' ')
    thelist = thelist.strip('\n')

    for element in thelist:
        if (element != ' ' and element != '\n'):
            current_number *= 10
            current_number += int(element)
        else:
            result.append(int(current_number))
            current_number = 0
    if (thelist[thelist.__len__() - 1] != '\n'):
        result.append(current_number)
    return result


def read_data():
    file_to_read_from = open('Data.txt', 'r')
    lines = file_to_read_from.readlines()
    result = []
    for i in range(0, len(lines), 2):
        info_about_student = lines[i].strip('\n').split(' ')
        if info_about_student[info_about_student.__len__() - 1] == '\n':
            info_about_student.pop()
        marks = encrypt_data(lines[i + 1])
        new_student = Student(info_about_student[0], info_about_student[1],
                              datetime.strptime(info_about_student[2], '%d.%m.%Y'), marks)
        result.append(new_student)
    file_to_read_from.close()
    return result


students = read_data()
for student in students:
    student.print()

print('Students with mark 2 in exam results')
students_with_failed_exam = [student for student in students if 2 in student.marks]
students_with_failed_exam.sort(key=lambda x: x.surname)
for student in students_with_failed_exam:
    student.print()
