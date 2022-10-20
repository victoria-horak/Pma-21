from classArrayList import *

tempArr = [100, 2, 3, 4, 56, 56]
list = ArrayList(tempArr)
print("List: ", list)

list.append(40, 45, 100, 100)
print("After append: ", list)

list.insert(2, 5, 6, 7)
print("After insert: ", list)

list.removeFirst(56,100)
print("After remove first: ",list)

list.remove(56, 100)
print("After remove: ", list)

list.pop(0)
print("After pop: ", list)

print("Index of 100: ", list.index(100))

print("Number of 100: ", list.count(100))

list.sort()
print("After sort: ", list)

list.reverse()
print("After reverse: ", list)

copyOfArrayList = list.copy()
copyOfArrayList.append(100, 100000)
print("Copy arr with append: ", copyOfArrayList)

print("List: ", list)

list.extend(list)
print("After extend: ", list)

list.clear()
print("After clear: ", list)
