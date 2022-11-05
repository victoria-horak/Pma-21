class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year


class Struct:
    def __init__(self, surname: str, name: str, date: Date, ball: list):
        self.surname = surname
        self.name = name
        self.date = date
        self.ball = ball


def repair(name_file):
    new_lines = ""
    with open(name_file, "r", encoding="utf8") as file:
        lines = file.readlines()
        for line in lines:
            for iterator in range(0, len(line)):
                if iterator == len(line) - 1:
                    new_lines += line[iterator]
                    break
                if line[iterator] == " " and line[iterator + 1] == " ":
                    continue
                new_lines += line[iterator]
    with open(name_file, "w", encoding="utf8") as file:
        file.write(new_lines)


def read_file(name_file):
    repair(name_file)
    with open(name_file, "r", encoding="utf8") as file:
        lines = file.readlines()
        list_text = []
        for line in lines:
            if len(line) < 2:
                continue
            line = line.split(" ")
            name = line[0]
            surname = line[1]
            date = Date(int(line[2]), int(line[3]), int(line[4]))
            ball = []
            for iterator in range(5, len(line)):
                if len(line[iterator]) > 0 and line[iterator] != "\n":
                    ball.append(int(line[iterator]))
            struct = Struct(name, surname, date, ball)
            list_text.append(struct)
    return list_text


name_file = "sources//data.txt"
my_list = read_file(name_file)
for iterator in my_list:
    print(iterator.surname, end=" ")
    print(iterator.name, end=" ")
    print(iterator.date.day, end=" ")
    print(iterator.date.month, end=" ")
    print(iterator.date.year, end=" ")
    print(iterator.ball)

print("--------------")
sorted_my_list = sorted(my_list, key=lambda x: x.surname)
flag = True
for iterator in sorted_my_list:
    if 2 in iterator.ball:
        print(iterator.surname, end=" ")
        print(iterator.name, end=" ")
        print(iterator.date.day, end=" ")
        print(iterator.date.month, end=" ")
        print(iterator.date.year, end=" ")
        print(iterator.ball)
        flag = False
if flag:
    print("There are no students with a grade of 2")
