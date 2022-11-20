def readData(fileName):
    dataDictionary = {}
    with open(fileName) as file:
        for line in file:
            cleanedLine = line.strip()
            if cleanedLine == "":
                continue
            words = line.split()
            if len(words) != 2:
                print("Incorrect line")
                continue
            dataDictionary[words[0]] = words[1]
    return dataDictionary


def getByKey(dictionary: dict, key):
    if key in dictionary:
        return dictionary[key]
    return "Cannot find value"


def getByValue(dictionary: dict, value):
    allValues = list(dictionary.values())
    if value in allValues:
        return list(dictionary.keys())[allValues.index(value)]
    return "Cannot find key"


data = readData("Chemical elements.txt")
print(data)
print(getByKey(data, "Aurum"))
print(getByValue(data, "O"))
