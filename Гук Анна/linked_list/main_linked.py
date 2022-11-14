from LinkedList import LinkedList
# from Node import Node
from Exception_linked import IndexException

try:
    list = LinkedList()
    list.append(2,2)
    print(list)
    list.append(3,2)
    print(list)
    list.remove_with_index(2)
    print(list)
    list.append(6,5,4,6,2,6)
    print(list)
    list.remove_one(6)
    print(list)
    list.remove_the_same(6)
    print(list)
    list.clear()
    print(list)


except IndexException as e:
    print(e)