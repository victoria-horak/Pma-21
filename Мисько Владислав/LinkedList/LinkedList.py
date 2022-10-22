from typing import TypeVar, Generic

T = TypeVar('T')

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList(Generic[T]):
    def __init__(self):
        self.root = None

    def initial_insert(self, value: T):
        current_node = Node(value)
        self.root = current_node

    def check_is_empty(self):
        return self.root is None

    def insert_at_beginning(self, value: T):
        if (self.check_is_empty()):
            self.initial_insert(value)
            return
        current_node = Node(value)
        current_node.next = self.root
        self.root.previous = current_node
        self.root = current_node

    def insert_at_end(self, value: T):
        if (self.check_is_empty()):
            self.initial_insert(value)
            return
        current_node = self.root
        while current_node.next is not None:
            current_node = current_node.next
        new_node = Node(value)
        current_node.next = new_node
        new_node.previous = current_node

    def insert_after_element(self, x: T, value: T):
        current_node = self.root
        while current_node is not None:
            if (current_node.value == x):
                break
            current_node = current_node.next
        if (current_node is None):
            print('Element is not present in the list')
            return
        new_node = Node(value)
        new_node.previous = current_node
        new_node.next = current_node.next
        if current_node.next is not None:
            current_node.next.previous = new_node
        current_node.next = new_node

    def insert_before_element(self, x: T, value: T):
        current_node = self.root
        while current_node is not None:
            if current_node.value == x:
                break
            current_node = current_node.next
        if current_node is None:
            print('Element is not present in the list')
            return
        new_node = Node(value)
        new_node.next = current_node
        new_node.previous = current_node.previous
        if current_node.previous is not None:
            current_node.previous.next = new_node
        current_node.previous = new_node

    def __str__(self):
        if (self.check_is_empty()):
            return 'there are no elements'
        else:
            result = ''
            current_node = self.root
            while (current_node is not None):
                result += str(current_node.value) + ' '
                current_node = current_node.next
            return result

    def delete_at_beginning(self):
        if (self.root is None):
            print('there are no elements in list')
            return
        self.root = self.root.next
        self.root = None

    def delete_at_end(self):
        if (self.check_is_empty()):
            print('there are no elements in list')
        current_node = self.root
        while current_node is not None:
            current_node = current_node.next
        current_node.previous.next = None

    def delete(self, value: T):
        if self.check_is_empty():
            print('there are no elements in list')
            return
        current_node = self.root
        while current_node.value != value and current_node.next is not None:
            current_node = current_node.next
        if current_node.previous is not None:
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous
        if current_node.next is not None:
            current_node.next.previous = current_node.previous
            current_node.previous.next = current_node.next

    def reverse(self):
        if (self.check_is_empty()):
            print('there are no elements in list')
        prev = None
        current_node = self.root
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node 
        self.root = prev