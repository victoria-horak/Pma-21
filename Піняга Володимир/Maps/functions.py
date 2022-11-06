def read_from_file(file_name):  # name - key, mark - value
    elements = dict()
    with open(file_name, "r") as file:
        for string in file:
            temp = []
            for element in string.strip().split(" "):
                temp.append(element)
            elements[temp[0]] = temp[1]

    return elements


def find_name(elements, name):
    if name in elements.keys():
        print(str(name) + " : " + str(elements[name]))
    else:
        print("This name is not present in elements dictionary")


def find_mark(elements, mark):
    if mark in elements.values():
        for name, designation in elements.items():
            if mark == designation:
                print(str(elements[name]) + " : " + str(name))
                # break
    else:
        print("This name is not present in elements dictionary")
