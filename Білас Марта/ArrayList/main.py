from ArrayList import *

array = ArrayList()
array.append(2, 2, 2, 2, 3)
print("array after append", array)
print("capacity:"+str(array.capacity()))
array.eraseFirst(2)
print("array after erase first entry of 2", array)
print("capacity:"+str(array.capacity()))
print("fourth element:" + str(array.at(3)))
array.popFront(2)
print("array after pop 2 first element", array)
print("capacity:"+str(array.capacity()))
array.popBack(3)
print("array after pop 3 last element", array)
print("capacity:"+str(array.capacity()))
array.append(2, 2, 2, 2, 3)
print(array)
print("capacity:"+str(array.capacity()))
array.eraseAll(2)
print("array after erase all entries of 2", array)
print("capacity:"+str(array.capacity()))
array.clear()
print("array after clear", array)
array.append(3)
print(array)
