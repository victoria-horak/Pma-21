from DoublyLinkedList import Node
from DoublyLinkedList import DoublyLinkedList
from IndexException import IndexException

try:
    doubleList = DoublyLinkedList()
    print("Append:")
    doubleList.append(3,4,5,6,2,3,7,8,8,10,8,5,2,2,8)
    print(doubleList)
    print("Remove one insertion:")
    doubleList.removeOne(3)
    print(doubleList)
    print("Remove all insertions:")
    doubleList.removeAll(8)
    print(doubleList)
    print("Remove by index:")
    doubleList.removeByIndex(3)
    print(doubleList)
    print("Clear:")
    doubleList.clear()
    print(doubleList)
except IndexException as e:
    print(e)

