from IndexException import IndexException


class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, data=None):
        node = Node(data)
        self.head = node
        self.tail = node
        self.head.next = node
        self.head.prev = node
        self.tail.next = node
        self.tail.prev = node

    def listLength(self):
        currentNode = self.head
        length = 0
        if currentNode.value is not None:
            while currentNode is not None:
                length += 1
                currentNode = currentNode.next
        return length

    def __str__(self):
        if self.head is None:
            print("Linked list is empty")
        currentNode = self.head
        temp = ""
        for i in range(self.listLength()):
            temp += str(currentNode.value) + ","
            currentNode = currentNode.next
        temp = temp[:-1]
        return "[" + temp + "]"

    def clear(self):
        self.__init__()

    def append(self, *values):
        for value in values:
            if self.head.value is None:
                self.__init__(value)
            else:
                item = Node(value)
                self.tail.next = item
                item.previous = self.tail
                self.tail = item

    def removeOne(self, key):
        if (self.head != None and self.head.value == key):
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None
        else:
            temp = self.head
            if (temp != None):
                while (temp.next != None):
                    if (temp.next.value == key):
                        nodeToDelete = temp.next
                        temp.next = temp.next.next
                        if (temp.next != None):
                            temp.next.prev = temp
                        nodeToDelete = None
                        break
                    else:
                        temp = temp.next


    def removeAll(self, key):
        while (self.head != None and self.head.value == key):
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None
        temp = self.head
        if (temp != None):
            while (temp.next != None):
                if (temp.next.value == key):
                    nodeToDelete = temp.next
                    temp.next = temp.next.next
                    if (temp.next != None):
                        temp.next.prev = temp
                    nodeToDelete = None
                else:
                    temp = temp.next

    def removeByIndex(self, index):
        if index < 0 or index > self.listLength():
            raise IndexException("INCORRECT INDEX!!!!!")
        if index == 0:
            self.head.prev = self.head
            self.head = self.head.next
        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                iterator.next = iterator.next.next
                iterator.prev = iterator.next
                break
            iterator = iterator.next
            count += 1
