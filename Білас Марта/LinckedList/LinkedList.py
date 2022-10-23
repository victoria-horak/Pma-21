from Node import *


class LinkedList:
    def __init__(self, data=None):
        node = Node(data)
        self.head = node
        self.tail = node
        self.head.next = self.tail
        self.tail.previous = self.head
        self.tail.next = None
        self.head.previous = None

    def __len__(self):
        count = 0
        currentNode = self.head
        if currentNode.value is not None:
            while currentNode is not None:
                count += 1
                currentNode = currentNode.next
        return count

    def __str__(self):
        if self.head.value is not None:
            current = self.head
            result = 'list [' + str(current.value) + ', '
            while current.next is not None:
                current = current.next
                result += str(current.value) + ', '
            result = result[0:result.len() - 2]
            return result + ']'
        return 'list []'

    def clear(self):
        self.__init__()

    def at(self, index):
        try:
            tempIndex = 0
            maxIndex = self.__len__() - 1
            currentNode = self.head
            if not isinstance(index, int):
                raise ValueError
            if index < 0:
                index = self.__len__() + index
            if index > maxIndex or index < 0:
                raise IndexError
            while currentNode.value is not None:
                if tempIndex != index:
                    tempIndex += 1
                    currentNode = currentNode.next
                else:
                    return currentNode.value
        except IndexError:
            print("out of range")
        except ValueError:
            print("index has to be int")

    def pushBack(self, *values):
        for value in values:
            if self.head.value is None:
                self.__init__(value)
            else:
                item = Node(value)
                self.tail.next = item
                item.previous = self.tail
                self.tail = item

    def eraseFirst(self, *values):
        for value in values:
            currentNode = self.head
            while currentNode is not None:
                previousNode = currentNode.previous
                nextNode = currentNode.next
                if currentNode.value == value:
                    if previousNode is not None:
                        previousNode.next = nextNode
                        if nextNode is not None:
                            nextNode.previous = previousNode
                    else:
                        self.head = nextNode
                        if nextNode is not None:
                            nextNode.previous = None
                    break
                currentNode = nextNode

    def eraseAllEntries(self, *values):
        for value in values:
            currentNode = self.head
            while currentNode is not None:
                previousNode = currentNode.previous
                nextNode = currentNode.next
                if currentNode.value == value:
                    if previousNode is not None:
                        previousNode.next = nextNode
                        if nextNode is not None:
                            nextNode.previous = previousNode
                    else:
                        self.head = nextNode
                        if nextNode is not None:
                            nextNode.previous = None
                currentNode = nextNode

    def popFront(self, number):
        try:
            if not isinstance(number, int):
                raise ValueError
            if self.head.value is None:
                raise IndexError
            for i in range(number):
                nextNode = self.head.next
                self.head = nextNode
                nextNode.previous = None
        except IndexError:
            print("list is empty")
        except ValueError:
            print("wrong index type")

    def popBack(self, number):
        try:
            if not isinstance(number, int):
                raise ValueError
            if self.head.value is None:
                raise IndexError
            for i in range(number):
                previousNode = self.tail.previous
                self.tail = previousNode
                previousNode.next = None
        except IndexError:
            print("list is empty")
        except ValueError:
            print("wrong index type")

    def search(self, value):
        currentNode = self.head
        index = 0
        result = []
        while currentNode is not None:
            if currentNode.value == value:
                result.append(index)
            currentNode = currentNode.next
            index = index + 1
        if len(result) == 0:
            result = "there is not such number in this list"
        return result
