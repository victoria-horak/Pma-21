def inputFromFile(fileName):
    file = open(fileName)
    lines = file.readlines()
    Dictionary = dict()
    for line in lines:
        dateFromLine = line.strip().split(",")
        if len(dateFromLine) == 2:
            Dictionary.update({dateFromLine[0]: dateFromLine[1]})
    return Dictionary


elements = inputFromFile("Data.txt")
print("All elements by element:")
for element in elements:
    print(element + " : " + elements[element])

givenElement = input("Enter element symbol of which you want to see: ")
print(givenElement + " : " + elements.get(givenElement, "there is no such element."))

givenKey = input("Enter key: ")
elementUnderKey = "No such element"
for element in elements:
    if elements[element] == givenKey:
        elementUnderKey = element
        break
print(givenKey + " : " + elementUnderKey)
