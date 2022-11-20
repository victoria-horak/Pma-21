from Student import *

file = open('text.txt', 'r')
data = file.read().split('\n')
student = []
for i in range(len(data)):
    lines = data[i].split()
    date = [int(lines[2]), int(lines[3]), int(lines[4])]
    grades = []
    for i in range(5, len(lines)):
        grades.append(int(lines[i]))
    student.append(Student(date, lines[0], lines[1], grades))

print("All student:")
for i in range(len(student)):
    print(student[i])

for i in range(1, len(student)):
    for j in range(len(student) - i):
        if student[j].first_name == student[j + 1].first_name:
            if student[j].last_name > student[j + 1].last_name:
                student[j], student[j + 1] = student[j + 1], student[j]
        elif student[j].first_name > student[j + 1].first_name:
            student[j], student[j + 1] = student[j + 1], student[j]

print("Students that have 2:")
for i in range(len(student)):
    if student[i].is_two():
        print(student[i])
file.close()