from StudentClass import Student
from NoSuchStudentsException import NoSuchStudentsException


def read(fileName):
    studentsList = []
    with open(fileName, 'r') as file:
        for student in file:
            thisStudent = student.split(',')
            firstName = thisStudent[0]
            lastName = thisStudent[1]
            birthday = thisStudent[2]
            marks = thisStudent[3].split(' ')
            studentsList.append(Student(firstName, lastName, birthday, marks))
        return studentsList


def sort(studentsList):
    for i in range(len(studentsList)):
        for j in range(len(studentsList) - i - 1):
            if studentsList[j].lastName > studentsList[j + 1].lastName:
                temp = studentsList[j]
                studentsList[j] = studentsList[j + 1]
                studentsList[j + 1] = temp
    return studentsList


def markTwo(studentsList):
    studentsWithTwo = []
    for student in studentsList:
        if '2' in student.marks:
            studentsWithTwo.append(student)
    if len(studentsWithTwo) > 0:
        studentsWithTwo = sort(studentsWithTwo)
        return studentsWithTwo
    else:
        raise NoSuchStudentsException("No such students!!!")


print("All students:")
studentsList = read("students.txt")
sort(studentsList)
for i in studentsList:
    print(i)

try:
    print("\nStudents with mark 2: ")
    studentsWithTwo = markTwo(studentsList)
    for i in studentsWithTwo:
        print(i)
except NoSuchStudentsException as e:
    print(e)
