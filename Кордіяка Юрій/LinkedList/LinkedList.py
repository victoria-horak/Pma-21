from Node import *
from IncorrectIndexException import IncorrectIndexException


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is not None:
            current = self.head
            result_str = 'DoubleLinkedList [\n' + str(current.data) + '\n'
            while current.next is not None:
                current = current.next
                result_str += str(current.data) + '\n'
            return result_str + ']'
        return 'DoubleLinkedList []'



    def is_empty(self):
        return self.head is None

    def insert_begin(self, node_data=None):
        if type(node_data) is list:
            iterator = len(node_data) - 1
            while iterator >= 0:
                self.insert_begin(node_data[iterator])
                iterator = iterator - 1
        else:
            newNode = Node(node_data)
            newNode.next = self.head
            if self.head is not None:
                self.head.prev = newNode
                self.head = newNode
            else:
                self.head = newNode

    def insert_end(self, data=None):
        if type(data) is list:
            for iterator in range(len(data)):
                self.insert_end(data[iterator])
        else:
            if self.head is None:
                new_node = Node(data)
                self.head = new_node
                return
            current = self.head
            while current.next is not None:
                current = current.next
            new_node = Node(data)
            current.next = new_node
            new_node.prev = current

    def list_length(self):
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.getNext()
        return counter

    def print_list(self):
        current = self.head
        while current is not None:
            if current != self.head:
                print('<->', current.getData(), end=' ')
            else:
                print(current.getData(), end=' ')
            current = current.getNext()
        print()

    def clear(self):
        self.__init__()
        self.insert_begin()

    def remove_in_index(self, input_index):
        if input_index < 0 or self.list_length() <= input_index:
            raise IncorrectIndexException("You input incorrect index")
        elif input_index == 0:
            self.head = self.head.next
        else:
            index = 0
            current = self.head
            while current:
                if index == input_index - 1:
                    current.next = current.next.next
                    return
                current = current.next
                index += 1

    def insert_after(self, from_index, data_list):
        if from_index < 0 or from_index >= self.list_length():
            raise IncorrectIndexException("You input incorrect index")
        else:
            current = self.head
            index = 0
            if 0 > from_index > self.list_length():
                raise IncorrectIndexException("You input incorrect index")
            while from_index != index:
                current = current.next
                index += 1
            for data in data_list:
                self.insert_in_index(index, data)
                index += 1

    def insert_in_index(self, input_index, data):
        if input_index < 0 or self.list_length() <= input_index:
            raise IncorrectIndexException("You input incorrect index")
        if input_index == 0:
            self.insert_begin(data)
            return
        index = 0
        current = self.head
        while current:
            if index == input_index - 1:
                node = Node(data, current.next)
                current.next = node
                return
            current = current.next
            index += 1

    def remove_first(self, data):
        current = self.head
        if current is not None:
            for index in range(self.list_length()):
                if current.data == data:
                    self.remove_in_index(index)
                    return
                current = current.next
        else:
            print("Your double linked list is empty")
            return
        print("Specified element does not belong to this double linked list")

    def remove_all(self, data):
        current = self.head
        counter = 0
        if current is not None:
            for index in range(self.list_length()):
                if current.data == data:
                    self.remove_first(data)
                    counter += 1
                current = current.next
        else:
            print("Your double linked list is empty")
            return
        if counter == 0:
            print("You input incorrect data")
