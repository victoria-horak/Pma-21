from LinkedList import *


linked_list = LinkedList()
print("Before insert:")
if linked_list.isEmpty(): print("Linked list is empty")
else: print("Linked list is not empty")
linked_list.insertAtBeginning(195)
linked_list.insertAtEnd(8576)
linked_list.insertAtEnd(123)
print("After insert:")
if linked_list.isEmpty(): print("Linked list is empty")
else: print("Linked list is not empty")
linked_list.printLlist()
print('Searching "123":')
if linked_list.searchingElementBool(123): print("Index of required item =", linked_list.searchingElement(123))
print("Len of linked list =", linked_list.listLength())
linked_list.insertAtEnd()
linked_list.insertAtIndex(2, 'hello world')
linked_list.reverse()
linked_list.printLlist()
linked_list.deleteAtIndex(1)
linked_list.printLlist()
linked_list.clear()
print("After delete:")
if linked_list.isEmpty(): print("Linked list is empty")
else: print("Linked list is not empty")
linked_list.printLlist()
