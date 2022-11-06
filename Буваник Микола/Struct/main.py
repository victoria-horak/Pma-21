from Student import Student


def searcherStudent(arr):
    newArr = []
    for element in arr:
        k = 0
        for iterator in element.grades:
            if iterator == 2:
                k += 1
        if k > 0:
            newArr.append(element)
    return newArr


arr = []
with open("data.txt") as file:
    for line in file:
        student = Student("", "", [], [])
        student.readFromString(line)
        arr.append(student)
for i in arr:
    print(i)
new_arr = searcherStudent(arr)
print("\n Student who have 2 grade")
for i in new_arr:
    print(i)
new_arr.sort(key=lambda student: student.firstName)
print("\n Student who have 2 grade sorted by Firstname")
for i in new_arr:
    print(i)
