class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return 'Node ['+str(self.data)+']'

    def setData(self, data):
        self.data = data
        return self.data

    def getData(self):
        return self.data

    def setNext(self, next_node):
        self.next = next_node

    def getNext(self):
        return self.next

    def setPrev(self, prev_node):
        self.prev = prev_node

    def getPrev(self):
        return self.prev
