from ClassStudent import Student
from ClassBirthday import Birthday


def read_from_file(fileName):
    created = ""
    with open(fileName, 'r') as file:
        lines = file.readlines()
        for string in lines:
            for iterator in range(0, len(string)):
                if string[iterator] == " " and string[iterator+1] == " ":
                    continue

                if iterator == len(string) - 1:
                    created += string[iterator]
                    break
                created += string[iterator]

    with open(fileName, 'r') as file:
        student_list = []
        lines = file.readlines()
        for string in lines:
            if len(string) < 2:     # if string is ' ' or letter
                continue
            string = string.split(" ")
            name = string[0]
            last_name = string[1]
            birth_date = Birthday(int(string[2]), int(string[3]), int(string[4]))
            grades = []
            for iterator in range(5, len(string)):
                if len(string[iterator]) > 0 and string[iterator] != "\n":
                    grades.append(int(string[iterator]))
            student = Student(name, last_name, birth_date, grades)
            student_list.append(student)

    with open(fileName, 'w') as file:
        file.write(created)

    return student_list


def print_info(list_students):
    for iterator in list_students:
        print(iterator.name,  iterator.last_name, str(iterator.birth_date.day) + "." +
              str(iterator.birth_date.month) + "." + str(iterator.birth_date.year), iterator.grades)


def sort_list(sort_by):
    return sort_by.last_name


def students_with_grade2(list_students):
    grade = True
    for it in list_students:
        if 2 in it.grades:
            print(it.name, it.last_name, str(it.birth_date.day) + "." +
                  str(it.birth_date.month) + "." + str(it.birth_date.year), it.grades)
            grade = False

    if grade:
        print("There aren't such students who have a grade '2'")
