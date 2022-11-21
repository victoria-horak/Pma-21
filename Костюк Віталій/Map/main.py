def getSymbol(input_dictionary: dict, input_symbol: str):
    if input_symbol in input_dictionary:
        return input_dictionary[input_symbol]
    for input_symbol in range(len(input_dictionary)):
        if input_dictionary.get(input_symbol) is None:
            return "Input key in your dictionary"
    return "There is no entered element in the dictionary"


def getValue(input_dictionary: dict, input_value: str):
    result = []
    for element in dictionary:
        if input_dictionary.get(element) == input_value:
            result.append(element)
    if len(result) == 0:
        for element in dictionary:
            if input_dictionary.get(element) is None:
                return element
    if len(result) == 0:
        result.append("There is no entered element in the dictionary")
    return result


dictionary = {
    None: "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "Be": None,
    "B": "Beryllium",
    "C": "Carbon",
    "N": "Nitrogen",
    "O": "Oxygen",
    "F": "Fluorine",
    "Ne": "Neon",
    "O1": "Oxygen"
}

print(dictionary)
symbol = input("Input symbol : ")
print(getSymbol(dictionary, symbol))

value = input("Input value : ")
print(getValue(dictionary, value))
