
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

    def delete(self):
        if self.prev != None:
            if self.next != None:
                self.next.prev = self.prev
            self.prev.next = self.next
        else:
            if self.next != None:
                self.next.prev = None
