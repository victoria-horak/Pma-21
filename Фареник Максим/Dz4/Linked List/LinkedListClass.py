from IndexException import IndexException

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length
    
    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
           lastNode = self.head
           while True:
               if lastNode.next is None:
                    break
               lastNode = lastNode.next
           lastNode.next = newNode

    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def insertAt(self, newNode, index):
        if index < 0 or index > self.listLength():
            raise IndexException("INCORRECT INDEX!!!!")
        elif index == 0:
            return self.insertHead(newNode)
        currentNode = self.head
        currentIndex = 0
        while True:
            if currentIndex == index:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentIndex += 1

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("Linked list is empty")

    def deleteAt(self, index):
        if index < 0 or index >= self.listLength():
            raise IndexException("INCORRECT INDEX!!!!")
        currentNode = self.head
        currentIndex = 0
        if self.isListEmpty() is False:
            if index == 0:
                return self.deleteHead
            while True:
                if currentIndex == index:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentIndex += 1

    def find(self, data):
        currentNode = self.head
        flag = 0
        count = 0
        while currentNode is not None:
            if currentNode.data == data:
                flag = 1
                return count
            count += 1
            currentNode = currentNode.next
        if flag == 0:
            print("Item is not found")
    
    def clear(self):
        self.__init__()
        
    def reverse(self):
        previousNode = None
        currentNode = self.head
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        self.head = previousNode

    def __str__(self):
        if self.head is None:
            print("Linked list is empty")
        currentNode = self.head
        temp = ""
        for i in range (self.listLength()):
            temp += str(currentNode.data) + ","
            currentNode = currentNode.next
        temp = temp[:-1]
        return "[" + temp + "]"

