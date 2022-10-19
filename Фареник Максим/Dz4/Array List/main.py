from ArrayClass import ArrayList
from IndexException import IndexException

try:
    arr = ArrayList()

    # Append
    arr.append(3)
    arr.append(4)
    arr.append(77)
    arr.append(6)
    arr.append(50)
    print(arr)

    #Insert
    arr.insert(0, 50)
    print(arr)

    #Removing by index
    arr.removeByIndex(1)
    print(arr)

    #Removing by value
    arr.remove(50)
    print(arr)

    #Pop
    arr.pop()
    print(arr)

    #Clear
    arr.clear()
    print(arr)

    #Find item
    arr.append(3)
    arr.append(4)
    arr.append(77)
    arr.append(6)
    arr.append(50)
    print(arr)
    print(arr.find(4))
except IndexException as e:
    print(e)
