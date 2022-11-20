from Node import *


class DoubleLinkedList:

    def __init__(self, *args):
        self.start = None
        self.end = None
        for i in args:
            self.add_in_the_end(i)

    def add_node(self, data):
        new_node = Node(data, None, None)

        if self.start is None:
            self.start = self.end = new_node
        else:
            new_node.previous = self.end
            new_node.next = None
            self.end.next = new_node
            self.end = new_node

    def add_in_the_beginning(self, number):
        new_node = Node(number, None, None)
        if self.start is None:
            self.start = new_node
        else:
            self.start.previous = new_node
            new_node.next = self.start
            self.start = new_node

    def add_few_in_the_beginning(self, *args):
        for i in args:
            self.add_in_the_beginning(i)

    def print_list(self):
        temp = self.start
        if temp is not None:
            print("The list contains:", end=" ")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")

    def add_in_the_end(self, number):
        new_node = Node(number, None, None)
        if self.start is None:
            self.start = self.end = new_node
            self.start.previous = None
            self.end.next = None
        else:
            self.end.next = new_node
            new_node.previous = self.end
            self.end = new_node
            self.end.next = None

    def add_few_in_the_end(self, *args):

        for i in args:
            self.add_in_the_end(i)

    def delete_first_entry_of_element(self, num):
        list = DoubleLinkedList()
        current_node = self.start
        count = 0
        while current_node is not None:
            if current_node.data != num or count > 0:
                list.add_in_the_end(current_node.data)
            else:
                count += 1
            current_node = current_node.next
        self.start = list.start
        self.end = list.end

    def delete_first_entry_of_few(self, *args):
        for i in args:
            self.delete_first_entry_of_element(i)

    def delete_the_same_elements(self, num):
        list = DoubleLinkedList()
        current_node = self.start
        while current_node is not None:
            if current_node.data != num:
                list.add_in_the_end(current_node.data)
            current_node = current_node.next
        self.start = list.start
        self.end = list.end

    def delete_different_elements(self, *args):
        for i in args:
            self.delete_the_same_elements(i)

    def iterator(self, num):
        count = 0
        current_node = self.start
        while True:
            if count == num:
                print(current_node.data)
                break
            count += 1
            current_node = current_node.next

    def reverse_node(self):
        list = DoubleLinkedList()
        temp = self.start
        while temp is not None:
            list.add_in_the_beginning(temp.data)
            temp = temp.next
        list.print_list()

    def clear(self):
        self.start = None
        self.end = None
