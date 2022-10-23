from array_list import ArrayList
from exception import Exception_array

try:
    array = ArrayList()


    print("--APPEND-- ")
    array.append(4)
    array.append(6)
    array.append(9)
    array.append(7)
    array.append(2)
    array.append(0)
    array.append(44)
    array.append(11)
    print(array)
    print("Next element after 4:")
    print(array.next())

    print("--INSERT-- ")
    array.insert(2, 5)
    print(array)

    print("--REMOVE ELEMENT-- ")
    array.remove_element(4)
    print(array)
    print("--REMOVE ELEMENT BY INDEX-- ")
    array.remove_element_by_index(4)
    print(array)

    print("--POP-- ")
    array.pop()
    print(array)

    print("--FIND ELEMENT-- ")
    array.append(9)
    array.append(5)
    array.append(8)
    array.append(10)
    array.append(11)
    print(array)
    print("index of  element 9:")
    print(array.find(9))
    print("index of  element 10:")
    print(array.find(10))
    print("--CLEAR-- ")
    array.clear()
    print(array)
except Exception_array as e:
    print(e)