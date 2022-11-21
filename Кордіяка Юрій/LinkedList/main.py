from LinkedList import *
from IncorrectIndexException import IncorrectIndexException

print("Before insert : ")
linked_list = LinkedList()
print("List is empty ")
linked_list.print_list()
print("Insert to Begin : ")
linked_list.insert_begin(10)
linked_list.print_list()
print("Insert to Begin few elements : ")
linked_list.insert_begin([1, 2, 3])
linked_list.print_list()
print("Insert in the end : ")
linked_list.insert_end(12)
linked_list.print_list()
print("Insert in the end few elements: ")
linked_list.insert_end([4, 3])
linked_list.print_list()
try:
    print("Insert few elements : ")
    linked_list.insert_after(1, [23, 44, 55, 66])
    linked_list.print_list()
except IncorrectIndexException as e:
    print(e)

try:
    print('Remove at index 2 : ')
    linked_list.remove_in_index(2)
    linked_list.print_list()
except IncorrectIndexException as e:
    print(e)

print('Remove first entry 2 : ')
linked_list.remove_first(2)
linked_list.print_list()
print('Remove all entries 3 : ')
linked_list.remove_all(3)
linked_list.print_list()

