from InvalidExce import InvalidIndex
# node - ���������: value - �������� � ������, next- ����� �� �������� �������, previous - �� ���������
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList():
    #�����������
    def __init__(self):
        self.root = None
    #�������� � ������ ���
    def insert_in_empty(self, value):
        current_node = Node(value)
        self.root = current_node
    #�������� �� �������
    def check_is_empty(self):
        return self.root is None
    #������ �� ��������
    def remove_index(self, index):
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
    #�������� �� �������
    def insert_at_start(self, value):
        if (self.check_is_empty()):
            self.insert_in_empty(value)
            return
        current_node = Node(value)
        current_node.next = self.root
        self.root.previous = current_node
        self.root = current_node
    #�������� ����� �������� � �����
    def insert_values(self, elements):
         for element in elements:
             self.insert_at_end(element)
    # ������� �������
    def length(self):
        result = 0
        current_node = self.root
        while current_node is not None:
            result += 1
            current_node = current_node.next
        return result
    #�������� �� �����
    def insert_at_end(self, value):
        if (self.check_is_empty()):
            self.insert_in_empty(value)
            return
        current_node = self.root
        while current_node.next is not None:
            current_node = current_node.next
        new_node = Node(value)
        current_node.next = new_node
        new_node.previous = current_node
    #  ���������� ������ __str__
    def __str__(self):
        if (self.check_is_empty()):
            return 'List is empty'
        else:
            result = ''
            current_node = self.root
            while (current_node is not None):
                result += str(current_node.value) + ' '
                current_node = current_node.next
            return result
     # ������� �� �������
    def delete_at_beginning(self):
        if (self.root is None):
            print('List is empty')
            return
        self.root = self.root.next
    # ������� � ����
    def delete_at_end(self):
        if (self.check_is_empty()):
            print('List is empty')
            return
        current_node = self.root
        while current_node is not None:
            current_node = current_node.next
        current_node.previous.next = None
    #������� �� ��������� ������� ��������
    def delete(self, value):
        if self.check_is_empty():
            print('List is empty')
            return
        iterator = 0
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                self.remove_index(iterator)
            else:
                iterator += 1
            current_node = current_node.next
    #�����
    def clear(self):
        self.__init__()
    # ���������� ������, ��� ����������� �� �������
    def __getitem__(self, index):
        try:
            if (index < 0 or index >= self.length()):
                raise InvalidIndex('Incorrect index')
            counter = 0
            current_node = self.root
            while current_node is not None:
                if counter == index:
                    break
                current_node = current_node.next
                counter += 1
            return current_node
        except InvalidIndex as e:
            print(str(e))