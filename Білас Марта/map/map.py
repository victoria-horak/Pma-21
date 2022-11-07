def outputFromFile(elements):
    with open("data.txt") as file:
        try:
            for line in file:
                if not line.isspace():
                    line = line.split(", ")
                    if line.__len__() == 2:
                        elements.update({line[0]: line[1][:-1]})
        except ValueError:
            print("wrong element type")


def addElement(elements, key, element):
    try:
        if key is None:
            raise TypeError
        elements.update({elements[key]: key})
    except TypeError:
        print("key is None")


def change(elements):
    result = dict()
    for key in elements:
        result.update({elements[key]: key})
    return result


elements = dict()
outputFromFile(elements)
addElement(elements, None, "cafg")
print(elements)
key = input("enter name of element: ")
print("short name of ", key, ":", elements.get(key, "there is not such element"))
elements = change(elements)
print(elements)
key = input("enter symbol of element: ")
print("full name of ", key, ":", elements.get(key, "there is not such element"))
