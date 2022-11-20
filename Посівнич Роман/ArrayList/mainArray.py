from ClassArray import Array
from Invalid import Invalid

try:
    array = Array()

    print("Add elements: ")
    array.addElements(1, 2, 2, 4, 6, 8, 8, 8, 8, 12, 25)
    print(array)

    print("Add elements by index: ")
    array.addElementByIndex(4, 30)
    print(array)

    print("Delete last elements: ")
    array.deleteLastElement()
    print(array)

    print("Delete one insertion: ")
    array.deleteOneInsertion(8)
    print(array)

    print("Delete all specific elements: ")
    array.deleteAllSpecificElements(2, 8, 1)
    print(array)

    print("Delete by index: ")
    array.deleteByIndex(2)
    print(array)

except Invalid as e:
    print(e)
