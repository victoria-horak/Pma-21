from LinkedListClass import Node
from LinkedListClass import LinkedList
from IndexException import IndexException

linkedList = LinkedList()
try:
    #End insertion
    firstNode = Node(10)
    linkedList.insertEnd(firstNode)
    secondNode = Node(20)
    linkedList.insertEnd(secondNode)
    thirdNode = Node(30)
    linkedList.insertEnd(thirdNode)
    print("End insertion: ")
    print(linkedList)

    #Head insertion
    fourthNode = Node(4)
    linkedList.insertHead(fourthNode)
    print("Head insertion: ")
    print(linkedList)

    #Index insertion
    fifthNode = Node(68)
    linkedList.insertAt(fifthNode, 3)
    sixthNode = Node(15)
    linkedList.insertAt(sixthNode, 2)
    print("Index insertion: ")
    print(linkedList)

    #Reverse
    linkedList.reverse()
    print("Reverse list: ")
    print(linkedList)

    #End delete
    linkedList.deleteEnd()
    print("End delete: ")
    print(linkedList)

    #Head delete
    linkedList.deleteHead()
    print("Head delete: ")
    print(linkedList)

    #Index delete
    print("Index delete: ")
    linkedList.deleteAt(1)
    print(linkedList)

    #Find
    print("Finding the element in the list: ")
    print(linkedList.find(10))
    print("\n")
    #Clear
    print("Clear the list: ")
    linkedList.clear()
    print(linkedList)

except IndexException as e:
    print(e)

