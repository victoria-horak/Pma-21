from Student import *


def readDataFromFile(fileMame: str):
    file = ""
    try:
        file = open(fileMame)
    except FileNotFoundError as exc:
        print("Error: " + str(exc))
        exit()
    fileLines = file.readlines()
    listOfStudents = []
    for line in fileLines:
        splitOfLine = line.strip("\n ").split(",")
        if len(splitOfLine) != 4:
            continue
        marks = splitOfLine[3]
        splitMarks = marks.strip("\n ").split(";")
        intSplitMarks = [int(mark) for mark in splitMarks]
        newStudent = Student(splitOfLine[0], splitOfLine[1], int(splitOfLine[2]), list(intSplitMarks))
        listOfStudents.append(newStudent)
    return listOfStudents


students = readDataFromFile("StudentsData.txt")
for student in students:
    print(student)

print("\nStudents with two:")
studentWithTwo = [student for student in students if 2 in student.marks]

if len(studentWithTwo) != 0:
    studentWithTwo.sort(key=lambda element: element.Surname)
    for student in studentWithTwo:
        print(student)
else:
    print("No people with two.")
