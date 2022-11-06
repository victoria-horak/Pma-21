dictionary = {
    "Hydrogen": "H",
    "Helium": "He",
    "Lithium": "Li",
    "Beryllium": "Be",
    "Boron": "B",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Flourine": "F",
    "Neon": "Ne"
}


def searchByName(dictionaryName: dict, elementName: str):
    if elementName in dictionaryName:
        return dictionaryName[elementName]
    else:
        return "There is no such element"


def searchBySymbol(dictionaryName: dict, elementName: str):
    for element in dictionary:
        if dictionaryName.get(element) == elementName:
            return element
    else:
        return "There is no such element"


element = input("Input element name: ")
print(searchByName(dictionary, element))

element = input("Input element symbol: ")
print(searchBySymbol(dictionary, element))
