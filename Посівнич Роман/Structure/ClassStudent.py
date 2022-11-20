class Student:
    def __init__(self, surName, name, date_of_birth, marks=None):
        if marks is None:
            marks = []
        self.surName = surName
        self.name = name
        self.date_of_birth = date_of_birth
        self.marks = marks

    def __str__(self):
        return self.surName + " " + self.name + " " + self.date_of_birth + " " + ",".join(self.marks)


def read_from_file(fileName):
    with open(fileName) as file:
        students = []
        for line in file:
            cleanedLine = line.strip()
            if cleanedLine == "":
                continue
            words = line.split()
            if len(words) != 4:
                print("Incorrect line")
                continue
            name = words[0]
            surName = words[1]
            year = words[2]
            marks = words[3].split(",")
            student = Student(name, surName, year, marks)
            students.append(student)
        return students


studentsFromFile = read_from_file("student.txt")

for student in studentsFromFile:
    print(student)
print("\n")

filteredStudents = list(filter(lambda st: "2" in st.marks, studentsFromFile))

if len(filteredStudents) == 0:
    print("There are no students with a mark of 2.")

sortedStudents = sorted(filteredStudents, key=lambda sy: sy.surName)

for student in sortedStudents:
    print(student)
