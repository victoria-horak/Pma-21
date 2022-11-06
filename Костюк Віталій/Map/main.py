def getSymbol(input_dictionary: dict, input_symbol: str):
    if input_symbol in input_dictionary:
        return input_dictionary[input_symbol]
    return "There is no entered element in the dictionary"


def getValue(input_dictionary: dict, input_value: str):
    for element in dictionary:
        if input_dictionary.get(element) == input_value:
            return element
    return "There is no entered element in the dictionary"


dictionary = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "Be": "Beryllium",
    "B": "Beryllium",
    "C": "Carbon",
    "N": "Nitrogen",
    "O": "Oxygen",
    "F": "Fluorine",
    "Ne": "Neon"
}
print(dictionary)
symbol = input("Input symbol : ")
print(getSymbol(dictionary, symbol))

value = input("Input value : ")
print(getValue(dictionary, value))
