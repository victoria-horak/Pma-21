from student import Student


def readFile(name):
    file = open(name)
    arr = []
    for line in file:
        arrSplit = [x for x in line.strip().split(" ")]
        student = Student("", "", "", [])
        student.surname = arrSplit[0]
        student.name = arrSplit[1]
        student.dateOfBirth = arrSplit[2]
        student.gradesList = [int(x) for x in arrSplit[3:len(arrSplit)]]
        arr.append(student)
    return arr


def findStudent(stuArr):
    arr = []
    for student in stuArr:
        counter = 0
        for grade in student.gradesList:
            if grade == 2:
                counter += 1
        if counter > 0:
            arr.append(student)
    return arr


arrStu = readFile("student.txt")
for i in arrStu:
    print(i)
print("\n")
arrSorted = findStudent(arrStu)
for i in arrSorted:
    print(i)
arrSorted.sort(key=lambda student: student.surname)
print("\n")
for i in arrSorted:
    print(i)
