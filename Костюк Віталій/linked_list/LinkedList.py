class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.data)+']'

    def setData(self, data):
        self.data = data
        return self.data

    def setNext(self, next_node):
        self.next = next_node

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def hasNext(self):
        return self.next is not None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = 'LinkedList [\n' + str(current.value) + '\n'
            while current.next is not None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def isEmpty(self):
        return self.head is None

    def insertAtBeginning(self, node_data=None):
        newNode = Node()
        newNode.setData(node_data)

        if self.listLength() == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    def insertAtEnd(self, data=None):
        if self.head is not None:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def listLength(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def printLlist(self):
        current = self.head
        print("======\nStart:\n======")
        while current is not None:
            print(current.getData())
            current = current.getNext()

        print("======\nEnd\n======")

    def clear(self):
        self.__init__()

    def searchingElementBool(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def searchingElement(self, data):
        current = self.head
        count = 0
        while current is not None:
            if current.data == data:
                return count
            count += 1
            current = current.next

    def deleteAtIndex(self, input_index):
        if 0 > input_index > self.listLength():
            print("You input incorrect index")
            return
        if input_index == 0:
            self.head = self.head.next
        index = 0
        current = self.head
        while current:
            if index == input_index - 1:
                current.next = current.next.next
                break
            current = current.next
            index += 1

    def insertAtIndex(self, input_index, data):
        if 0 > input_index > self.listLength():
            print("You input incorrect index")
            return
        if input_index == 0:
            self.insertAtBeginning(data)
            return
        index = 0
        current = self.head
        while current:
            if index == input_index - 1:
                node = Node(data, current.next)
                current.next = node
                break
            current = current.next
            index += 1

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
