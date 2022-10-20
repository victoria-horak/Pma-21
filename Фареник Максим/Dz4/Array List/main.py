from ArrayClass import ArrayList
from IndexException import IndexException

try:
    arr = ArrayList()

    # Append
    print("Append: ")
    arr.append(3)
    arr.append(4)
    arr.append(77)
    arr.append(6)
    arr.append(50)
    print(arr)

    #Insert
    print("Insert: ")
    arr.insert(1, 50)
    print(arr)

    #Removing by index
    print("Remove by index: ")
    arr.removeByIndex(1)
    print(arr)

    #Removing by value
    print("Remove by value: ")
    arr.remove(50)
    print(arr)

    #Pop
    print("Pop: ")
    arr.pop()
    print(arr)

    #Clear
    print("Clear: ")
    arr.clear()
    print(arr)

    #Find item
    print("Find item: ")
    arr.append(3)
    arr.append(4)
    arr.append(77)
    arr.append(6)
    arr.append(50)
    print(arr)
    print(arr.find(-5))
except IndexException as e:
    print(e)
