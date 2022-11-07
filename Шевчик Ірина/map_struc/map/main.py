dictionary = {'Hydrogen': 'H',
              'Lithium': 'Li',
              'Berylliun': 'Be',
              'Carbon': 'C',
              'Nitrogen': 'N'}
print (dictionary)

def search(dictionaryName: dict, elementName: str):
    if elementName in dictionaryName:
        return dictionaryName[elementName]
    else:
        for element in dictionary:
            if dictionaryName.get(element) == elementName:
                return element
        else:
            return "There is no such element"

element = input("Enter elements Name: ")
print(search(dictionary, element))

