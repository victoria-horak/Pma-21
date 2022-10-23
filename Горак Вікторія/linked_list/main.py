class Node:

    def __init__(self, data, previous, next):
        self.data = data
        self.prev = previous
        self.next = next


class DoubleLinkedList:

    def __init__(self):
        self.start = None
        self.end = None

    def add_node(self, data):
        new_node = Node(data, None, None)

        if self.start is None:
            self.start = self.end = new_node
        else:
            new_node.previous = self.end
            new_node.next = None
            self.end.next = new_node
            self.end = new_node

    def delete_node(self, num):
        count = 0
        current_node = self.start

        while True:
            if count == num:
                if current_node.previous is not None:
                    current_node.previous.next = current_node.next
                    current_node.next.previous = current_node.previous
                else:
                    self.start = current_node.next
                    current_node.next.previous = None
                break
            count += 1
            current_node = current_node.next

    def show(self):
        if self.start is None:
            print(None)
        else:
            current_node = self.start
            while current_node is not None:
                if current_node.next is None:
                    print(current_node.data, end=" ")
                    break
                else:
                    print(current_node.data, end=" <---> ")
                    current_node = current_node.next

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
        bk=DoubleLinkedList()
        current_node = self.start
        count=0
        while current_node is not None:
            if current_node.data != num or count>0:
                bk.add_in_the_end(current_node.data)
            else:
                count+=1
            current_node=current_node.next
        self.start=bk.start
        self.end=bk.end

    def delete_first_entry_of_few(self, *args):
        for i in args:
            self.delete_first_entry_of_element(i)



    def delete_the_same_elements(self, num):
        bk = DoubleLinkedList()
        current_node = self.start
        while current_node is not None:
            if current_node.data != num:
                bk.add_in_the_end(current_node.data)
            current_node = current_node.next
        self.start = bk.start
        self.end = bk.end

    def delete_different_elements(self, *args):
        for i in args:
            self.delete_the_same_elements(i)

    def iterator(self, num):
        count = 0
        current_node = self.start
        while True:
            if count == num:
                print (current_node.data)
                break
            count += 1
            current_node = current_node.next

    def reverse_node(self):
        bk=DoubleLinkedList()
        temp=self.start
        while temp is not None:
            bk.add_in_the_beginning(temp.data)
            temp=temp.next
        bk.print_list()

    def clear(self):
        self.start = None
        self.end = None


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