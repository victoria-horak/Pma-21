class Node(object):
    def __init__(self, data, next = None, previous = None):
        self.data = data;
        self.next = next;
        self.previous = previous

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
    def initial_insert(self, value):
        current_node = Node(value)
        self.head = current_node
    def getitem(self, index):
        if (index < 0 or index >= self.length()):
               return
        counter = 0
        current_node = self.head
        while current_node is not None:
            if counter == index:
                break
            current_node = current_node.next
            counter += 1
        return current_node

    def insert_at_beginning(self, data):
        if (self.check_is_empty()):
            self.initial_insert(data)
            return
        current_node = Node(data)
        current_node.next = self.head
        self.head.previous = current_node
        self.head = current_node

    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp

    def check_is_empty(self):
        return self.head is None

    def insert_values(self, elements):
         for element in elements:
             self.insertAtEnd(element)

    def length(self):
        result = 0
        current_node = self.head
        while current_node is not None:
            result += 1
            current_node = current_node.next
        return result

    def delete_at_beginning(self):
        if (self.head is None):
            print('there are no elements in list')
            return
        self.head = self.head.next

    def delete_at_end(self):
        if (self.check_is_empty()):
            print('there are no elements in list')
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
        current_node.previous.next = None

    def remove_at(self, index):
        if index == 0:
            self.delete_at_beginning()
            return
        if index == self.length() - 1:
            self.delete_at_end()
            return
        current = self.getitem(index)
        if (current.previous is not None):
            previous = current.previous
            previous.next = current.next
        if (current.next is not None):
            next = current.next
            next.previous = current.previous

    def clear(self):
        self.__init__()

    def delete(self, data):
        temp = self.head
        if(temp.next != None):
            if(temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    temp = temp.next
                if(temp.next):
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    temp.previous.next = None
                    temp.previous = None
                return

        if (temp == None):
            return

    def str(self):
        if (self.check_is_empty()):
            return 'there are no elements'
        else:
            result = ''
            current_node = self.head
            while (current_node is not None):
                result += str(current_node.data) + ' '
                current_node = current_node.next
            return result
