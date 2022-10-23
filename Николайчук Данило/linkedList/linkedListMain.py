from linkedListClass import *

list = linkedList()

if list.isEmpty():
    print("List is empty.")
else:
    print("List isn`t empty.")

list.emplace_back(4, 5, 6, 7, 8, 9, 10)
print("List after adding element in end: ", list)

list.emplace_front(2, 1)
print("List after adding element in beggin: ", list)

list.emplace_in(2, 3)
print("List after adding element under index 2: ", list)

list.pop_back(3)
print("List after deleting 3 elements from end: ", list)

list.pop_front(3)
print("List after deleting 3 elements from begine: ", list)

list.removeIndex(2)
print("List after removing element with index 2: ", list)

otherList = linkedList()
otherList.emplace_back(1, 2, 3)
print("Other list: ", otherList)
list.emplace_ListFront(otherList)
print("List after adding other list in front: ", list)

otherList.clear()
print("Other list after clear: ", otherList)

otherList.emplace_back(8, 9, 10)
print("Other list: ", otherList)
list.emplace_ListInBack(otherList)
print("List after adding other list in back: ", list)

otherList.clear()
otherList.emplace_back(6)
print("Other list: ", otherList)
list.emplace_ListInIndex(5, otherList)
print("List after adding other list in 5 index: ", list)

list.removeFromTo(3, 7)
print("List after removing from 3 to 7 element: ", list)

print("Element with index 2: ", list.elementAt(2))

list.emplace_back(1, 2, 1)
list.emplace_front(2, 1, 5)
print("List: ", list)
list.removeFirstEntery(1, 2, 5)
print("List after removing first entery of 1,2,5: ", list)

list.removeAllEnteries(1)
print("List after remove all enteries of 1: ", list)

if list.seachBool(1):
    print("1 is present.")
else:
    print("1 isn`t in list.")

print("Place of first 4: ", list.searchPlace(4))

list.clear()
list.emplace_back(0, 9, 6, 3, 5, 7, 2, 7, 6, 1, 4, 8, 10)
print("List:            ", list)
list.sort()
print("List after sort: ", list)

list.reverse()
print("List after reverse: ", list)

list.swap(0, len(list) - 1)
print("List with swap element with index 1 and last: ", list)

print("List print from end to begin: ", end="")
list.printFromEnd()
