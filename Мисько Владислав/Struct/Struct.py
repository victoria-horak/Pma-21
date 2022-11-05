from Student import *

def parse_row(thelist):
    array = []
    currentNumber = 0
    for element in thelist:
        if (element != ' ' and element != '\n'):
            currentNumber *= 10
            currentNumber += int(element)
        else: 
            array.append(int(currentNumber))
            currentNumber = 0
    if (thelist[thelist.__len__() - 1] != '\n'):
        array.append(currentNumber)
    return array

def read_data():
    data_file = open('Data.txt', 'r')
    lines = data_file.readlines()
    list_of_students = []
    for iterator in range(0, len(lines), 2):
        data_about_student = lines[iterator].strip('\n').split(' ')
        if data_about_student[data_about_student.__len__() - 1] == '\n':
            data_about_student.pop()
        marks = parse_row(lines[iterator + 1])
        new_student = Student(data_about_student[0], data_about_student[1], data_about_student[2], marks)
        list_of_students.append(new_student)
    return list_of_students

students = read_data()
for element in students:
    element.print()


print('Students with mark 2 in exam results')
students_with_failed_exam = [student for student in students if 2 in student.marks]
students_with_failed_exam.sort(key = lambda x: x.surname)
for student in students_with_failed_exam:
    student.print()