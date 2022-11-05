from Student import Student
from NoPeopleException import *


def read_from_file(file_name):
    list_student = []
    last_name = ''
    name = ''
    date = ''
    score = 0
    with open(file_name, 'r') as file:
        for i in file:
            l = i.strip().split(',')
            if l != ['']:
                last_name = l[0]
                name = l[1]
                date = l[2]
                score = l[3].split(' ')
                list_student.append(Student(last_name, name, date, score))
    return list_student


def get_two(list_student):
    get_two = []
    for i in list_student:
        if '2' in i.score:
            get_two.append(i)
    if len(get_two) != 0:
        for i in range(0, len(get_two)):
            for j in range(0, len(get_two) - i - 1):
                if get_two[j].name > get_two[j + 1].name:
                    temp = get_two[j]
                    get_two[j] = get_two[j + 1]
                    get_two[j + 1] = temp
        return get_two
    else:
        raise NoPeopleException('none of the people got 2')


list_student = read_from_file('data')
student_get_two = get_two(list_student)
for i in student_get_two:
    print(i)
