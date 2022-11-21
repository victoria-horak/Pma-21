from NoneErrorExpresion import NoneErrorExpresion


def read_from_file(file_name):
    with open(file_name, encoding="utf-8") as file:
        dictionary = dict()
        for i in file:
            mass = [x for x in i.strip().split(" ")]
            dictionary[mass[0]] = mass[1]
    return dictionary


def keyIsNone(mass):
    for i in mass:
        if i is None:
            return mass.pop(None, None)


def find_key(dictionary, word):
    for i in dictionary:
        if dictionary.get(i) == word:
            return i
    raise NoneErrorExpresion("key is None")


def find_value(dictionary, word):
    for i in dictionary:
        if i == word:
            return dictionary.get(i)
    raise NoneErrorExpresion("value is None")


try:
    dictionary = read_from_file("data.txt")

    dictionary[None] = "something"
    dictionary["something"] = None
    keyIsNone(dictionary)
    print(dictionary)
    value = input("input value = ")
    print(find_key(dictionary, value))
    key = input("input key = ")
    print(find_value(dictionary, key))
    if key=="None":
        raise NoneErrorExpresion("Key is None")
except (NoneErrorExpresion) as e:
    print(e)
