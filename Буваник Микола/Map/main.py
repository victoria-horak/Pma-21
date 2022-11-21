from KeyUndefinedException import KeyUndefinedException


def KeySearcher(arr: dict, value: str):
    for iterator in arr:
        if str(arr.get(iterator)) == value:
            return iterator
    raise KeyUndefinedException("Key not found")


def ValueSearcher(arr: dict, key: str):
    if key == "None":
        return "Key is None"
    for iterator in arr:
        if str(iterator) == key:
            return arr.get(iterator)
    raise KeyUndefinedException("Value not found")


def keyIsNone(arr):
    for iterator in arr:
        if iterator is None:
            return arr.pop(None, None)


chemistryElement = {}
with open("data.txt") as f:
    for line in f:
        (key, val) = line.split()
        chemistryElement[key] = val
    chemistryElement[None] = "value"
    chemistryElement["Key"] = None
    keyIsNone(chemistryElement)
print(chemistryElement)
try:
    k = input()
    if k == "None":
        raise KeyUndefinedException("Key is None")
    print(ValueSearcher(chemistryElement, k))
    print(KeySearcher(chemistryElement, k))
except Exception as e:
    print(e)
