from Student import *
from NoStudentMark2 import *


def read_from_file(file_name):
    list_students = []
    with open(file_name, 'r') as file:
        for students in file:
            current_student = students.split(',')
            last_name = current_student[0]
            name = current_student[1]
            marks = current_student[2].split(' ')
            list_students.append(Student(last_name, name, marks))
    return list_students


def sort_students(list_students):
    for current_student in range(len(list_students)):
        for j in range(len(list_students) - current_student - 1):
            if list_students[j].name > list_students[j + 1].name:
                list_students[j], list_students[j+1] = list_students[j+1], list_students[j]
    return list_students


def didNotPass(list_students):
    list_student_mark_2 = []
    for current_student in list_students:
        if '2' in current_student.marks:
            list_student_mark_2.append(current_student)
    if len(list_student_mark_2) != 0:
        list_student_mark_2 = sort_students(list_student_mark_2)
        return list_student_mark_2
    else:
        raise NoStudentMark2("There are no students with a score of 2")


list_student = read_from_file('Data.txt')
print("All:")
for student in list_student:
    print(student)

print("\nDid not pass:")
try:
    student_get_two = didNotPass(list_student)
    for student in student_get_two:
        print(student)
except NoStudentMark2 as e:
    print(e)
