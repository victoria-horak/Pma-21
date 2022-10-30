from typing import TypeVar, Generic
from InvalidIndexException import InvalidIndexException

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

    def remove_at(self, index):
        if index == 0:
            self.delete_at_beginning()
            return
        if index == self.length() - 1:
            self.delete_at_end()
            return
        current = self[index]
        if (current.previous is not None):
            previous = current.previous
            previous.next = current.next
        if (current.next is not None):
            next = current.next
            next.previous = current.previous

    def insert_at_beginning(self, value: T):
        if (self.check_is_empty()):
            self.initial_insert(value)
            return
        current_node = Node(value)
        current_node.next = self.root
        self.root.previous = current_node
        self.root = current_node
       
    def insert_values(self, elements):
         for element in elements:
             self.insert_at_end(element)

    def length(self):
        result = 0
        current_node = self.root
        while current_node is not None:
            result += 1
            current_node = current_node.next
        return result
    
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
        iterator = 0
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                self.remove_at(iterator)
            else:
                iterator += 1
            current_node = current_node.next

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

    def clear(self):
        self.__init__()

    def __getitem__(self, index):
        try:
            if (index < 0 or index >= self.length()):
                raise InvalidIndexException('Incorrect index')
            counter = 0
            current_node = self.root
            while current_node is not None:
                if counter == index:
                    break
                current_node = current_node.next
                counter += 1
            return current_node
        except InvalidIndexException as e:
            print(str(e))