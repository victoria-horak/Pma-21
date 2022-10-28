from ArrayClass import ArrayList
from IndexException import IndexException

try:
    arr = ArrayList()

    # Append
    print("Append: ")
    arr.append(6,93,12,12,50,4, 4, 4,12,42,1)
    print(arr)

    # Insert
    print("Insert: ")
    arr.insert(1, 50)
    print(arr)

    #Pop
    print("Pop: ")
    arr.pop()
    print(arr)

    # Removing all insertions
    print("Removing all insertions: ")
    arr.removeAll(50,4)
    print(arr)

    # Removing by index
    print("Remove by index: ")
    arr.removeByIndex(5)
    print(arr)


    # Removing one insertion
    print("Removing one insertion: ")
    arr.removeOneInsertion(12,42)
    print(arr)


except IndexException as e:
    print(e)
