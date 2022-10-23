from Node import Node


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        if self.head is None:
            print(None)
        else:
            current = self.head
            while current is not None:
                if current.next is None:
                    print(current.data, end=" ")
                    break
                else:
                    print(current.data, end=" <-> ")
                    current = current.next

    def push_front(self, new_data):  # додає перед першим
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None

        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

    def push_back(self, new_data):  # додає після останнього
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None

        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node

    def get_front(self):  # повертає перший елемент (голову)
        if self.head is not None:
            return self.head.data
        else:
            print("List is empty")

    def get_back(self):  # повертає останній елемент (хвіст)
        if self.tail is None:
            print("List is empty")
        else:
            return self.tail.data

    def pop_front(self):  # видаляє перший елемент і повертає його
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            return temp.data

    def pop_back(self):  # видаляє останній елемент і повертає його
        if self.tail is None:
            print("List is empty")

        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            return temp.data

    def insert_after(self, temp_node, new_data):  # вставляє елемент після вказаного
        if temp_node is None:
            print("Given node is empty")

        if temp_node is not None:
            new_node = Node(new_data)
            new_node.next = temp_node.next
            temp_node.next = new_node
            new_node.previous = temp_node
            if new_node.next is not None:
                new_node.next.previous = new_node

            if temp_node == self.tail:  # перевірка чи новий елемент додався після останнього
                self.tail = new_node

    def insert_before(self, temp_node, new_data):  # вставляє елемент перед вказаним
        if temp_node is None:
            print("Given node is empty")

        if temp_node is not None:
            new_node = Node(new_data)
            new_node.previous = temp_node.previous
            temp_node.previous = new_node
            new_node.next = temp_node
            if new_node.previous is not None:
                new_node.previous.next = new_node

            if temp_node == self.head:  # перевірка чи новий елемент додався перед першим
                self.head = new_node
