from ArrayList import *
from IndexError import *

simple_list = [1, 2, 3, 4, 5, 6]
array_list = ArrayList(simple_list)

print("Start\n" + str(array_list))

try:
    array_list.deleteFromTo(1, 4)
    print("Delete from to:\n" + str(array_list))
except IndexError as e:
    print(e)

try:
    array_list.insertFrom(0, [98, 99, 100])
    print( "Insert from\n" + str(array_list))
except IndexError as e:
    print(e)

array_list.insertAtBegin(500)
print("Insert at begin\n" + str(array_list))

array_list.insertAtEnd(10)
print('Insert at end\n' + str(array_list))

try:
    array_list.deleteAtIndex(1)
    print('Delete at index\n' + str(array_list))
except IndexError as e:
    print(e)

print("500 is present ar array list?")
array_list.elementPresent(500)

try:
    array_list.insertAtIndex(1, 4)
    print('Insert at index\n' + str(array_list))
except IndexError as e:
    print(e)

array_list.reverse()
print('Reverse\n' + str(array_list))

array_list.sortArray()
print('Sort\n' + str(array_list))

array_list.deleteAllArray()
print('After deleting\n' + str(array_list))
