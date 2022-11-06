def read_from_file(file_name):
    with open(file_name, encoding="utf-8") as file:
        dictionary = dict()
        for i in file:
            mass = [x for x in i.strip().split(" ")]
            dictionary[mass[0]] = mass[1]
    return dictionary


def find_key(dictionary, word):
    for i in dictionary:
        if dictionary.get(i) == word:
            return i
    return "no key"


def find_value(dictionary, word):
    for i in dictionary:
        if i == word:
            return dictionary.get(i)
    return "no value"


dictionary = read_from_file("data.txt")
print(dictionary)
value = input("input value = ")
print(find_key(dictionary, value))
key = input("input key = ")
print(find_value(dictionary, key))
