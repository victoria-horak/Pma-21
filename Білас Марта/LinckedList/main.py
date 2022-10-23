from LinkedList import *

list = LinkedList(1)
list.pushBack(8)
print("list after first push back:", list)
list.pushBack(2, 9, 5, 10, 5)
list.pushBack(4, 2, 10)
print("list after second push back:", list)
print("list len:" + str(list.len()))

list.eraseFirst(4, 5)
print("list after erasing first 4 and 5", list)
list.eraseAllEntries(10)
print("list after erasing all entries of 10", list)

print("find third element: " + str(list.at(2)))
print("find index of 2" + str(list.search(2)))

list.popFront(2)
print("list after pop 2 first elements", list)
list.popBack(1)
print("list after pop 1 last element", list)

list.clear()
print("list after clear", list)
