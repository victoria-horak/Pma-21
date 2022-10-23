from LinkedList import DoublyLinkedList
from Node import Node

my_list = DoublyLinkedList()

my_list.push_front(12)
my_list.push_front(24)
my_list.push_front(48)
# my_list.print_list()

my_list.push_back(35)
my_list.push_back(123)
print("============LIST===========")
my_list.print_list()

print("\n============LIST AFTER popping front element===========")
my_list.pop_front()
my_list.print_list()

print("\n============LIST AFTER popping last element===========")
my_list.pop_back()
my_list.print_list()


