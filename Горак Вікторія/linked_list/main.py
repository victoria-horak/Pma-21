from LinkedList import *

linked_list = DoubleLinkedList()
linked_list.print_list()
linked_list.add_node(3451)

print('Add element in the beginning:')
linked_list.add_in_the_beginning(5)
linked_list.print_list()

print('Add few in the beginning:')
linked_list.add_few_in_the_beginning(4, 333, 3, 3, 3, 7)
linked_list.print_list()

print('Add element in the end:')
linked_list.add_in_the_end(9)
linked_list.print_list()

print('Add few in the end:')
linked_list.add_few_in_the_end(11, 67, 9)
linked_list.print_list()

print('Delete first entry of one element:')
linked_list.delete_first_entry_of_element(7)
linked_list.print_list()

print('Delete first entry of elements:')
linked_list.delete_first_entry_of_few(3, 4, 5)
linked_list.print_list()

print('Delete the same elements:')
linked_list.delete_the_same_elements(9)
linked_list.print_list()

print('Delete differents elements:')
linked_list.delete_different_elements(11, 67)
linked_list.print_list()

print('Reverse:')
linked_list.reverse_node()
linked_list.print_list()

print('Iteretor:')
linked_list.iterator(2)
linked_list.print_list()

print('Clear')
linked_list.clear()
linked_list.print_list()
