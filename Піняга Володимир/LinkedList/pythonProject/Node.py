class Node(object):
    def __init__(self, data):
        self.data = data  # adding an element to the node
        self.next = None  # Initially this node will not be linked with any other node
        self.previous = None  # It will not be linked in either direction

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_previous(self, previous):
        self.previous = previous
