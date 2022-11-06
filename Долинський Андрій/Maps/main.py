def readFile(name):
    file = open(name)
    dictionary = dict()
    for i in file:
        arr = i.strip().split(":")
        dictionary[arr[0]] = arr[1]
    return dictionary


def findProperty(arg, el):
    for i in arg:
        if i == el:
            return arg.get(i)
    return "Could not find any proper element"


def findKey(arg, el):
    for i in arg:
        if arg.get(i) == el:
            return i
    return "Could not find any proper element"


chemystry = readFile("names.txt")
# print(chemystry)
print(findKey(chemystry, "O"))
print(findProperty(chemystry, "Aluminum"))
