
dictionary = {
     None: "Cl",
    "мідь": None,
    'Гідроген': 'H',
    'Гелій': 'He',
    'азот': 'N',
    'актиній': 'Ac',
    'алюміній': 'Al'
}

def find_by_name(name):
    if name == None or name == "None":
        raise ValueError("Input cant be None")
    element = dictionary.get(name,"not in")
    if element == None:
        del dictionary[name]
    if element == None or element == "not in":
        return "No element with such name found"
    return element

def find_by_symbol(symbol):
    if symbol == None or symbol == "None":
        raise ValueError("Input cant be None")
    for key,value in dictionary.items():
        if value == symbol:
            name = key
            if name == None:
                del dictionary[name]
                return "No element with such symbol found"
            return name
    return "No element with such symbol found"

print(dictionary)
print(find_by_symbol("Cl"))
print(dictionary)
print(find_by_name("None"))
print(dictionary)
