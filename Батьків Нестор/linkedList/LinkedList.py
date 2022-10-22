from node import Node


class LinkedList:
    def __init__(self, inputvalue):
        self.parse(inputvalue)

    def parse(self, input_value):
        if isinstance(input_value, str):
            input_value = input_value.split(" ")

        if isinstance(input_value, list):
            current = None
            for elem in input_value:
                if current == None:
                    current = Node(elem)
                    self.head = current
                else:
                    current.next = Node(elem)
                    current.next.prev = current
                    current = current.next

    def get_last(self):
        last = None
        for elem in self:
            last = elem
        return last

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        result = ""
        for elem in self:
            result += f"{elem} <-> "
        return result[:-4]

    def insert_at_start(self, *elements):
        elements = elements[::-1]
        current = self.head
        for elem in elements:
            if current == None:
                current = Node(elem)
            else:
                current.prev = Node(elem)
                current.prev.next = current
                current = current.prev

        self.head = current
        return self

    def insert_at_end(self, *elements):
        current = self.get_last()
        if current == None:
            self.insert_at_start(*elements)
            return self

        for elem in elements:
            current.next = Node(elem)
            current.next.prev = current
            current = current.next
        return self

    def insert(self, index, *elements):
        if index == 0:
            self.insert_at_start(*elements)
            return self
        current = self[index-1]
        end = current.next
        for elem in elements:
            current.next = Node(elem)
            current.next.prev = current
            current = current.next

        current.next = end
        end.prev = current
        return self

    def reverse(self):
        current = self.head
        while current:
            if current.next == None:
                self.head = current
            current.next, current.prev, current = current.prev, current.next, current.next
        return self

    def __len__(self):
        length = 0
        for elem in self:
            length += 1
        return length

    def __getitem__(self, index):
        ind = 0
        if index < 0:
            index = len(self)+index
            if index < 0:
                raise IndexError()
        for elem in self:
            if ind == index:
                return elem
            ind += 1
        raise IndexError()

    def clear(self):
        self.head = None

    def remove(self, start_index, end_index=None):
        end_index = end_index or start_index+1
        if start_index ^ end_index < 0:
            length = len(self)
            if start_index < 0:
                start_index = length+start_index
            if end_index < 0:
                end_index = length+end_index
        if end_index < start_index:
            start_index, end_index = end_index, start_index

        start = self[start_index-1]
        end = self[end_index]
        if self[start_index] == self.head:
            self.head = end
            end.prev = None
        else:
            start.next = end
            end.prev = start
        return self

    def __contains__(self, element):
        for elem in self:
            if elem.value == element:
                return True
        return False

    def remove_entries(self, element, entries=1):
        for node in self:
            if node.value == element:
                if node.prev != None:
                    if node.next != None:
                        node.next.prev = node.prev
                    node.prev.next = node.next
                else:
                    self.head = node.next
                    if node.next != None:
                        node.next.prev = None
                entries -= 1
                if entries == 0:
                    break
        return self

    @classmethod
    def fromFile(cls, filePath):
        with open(filePath, "r") as file:
            return cls(file.read())

    @staticmethod
    def toFile_Static(l_list, filePath, overwrite=False):
        with open(filePath, "w" if overwrite else "a") as file:
            file.write(str(l_list) + "\n")

    def toFile(self, filePath, overwrite=False):
        self.toFile_Static(self, filePath, overwrite)
