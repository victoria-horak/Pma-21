from node import Node


class LinkedList:
    def __init__(self, inputvalue):
        self.head = self.parse(inputvalue) if inputvalue else None

    def parse(self, input_value):
        if isinstance(input_value, str):
            input_value = input_value.split(" ")
        if isinstance(input_value, list):
            input_value = input_value[::-1]
            current = None
            for elem in input_value:
                current = Node(elem, current)
            return current

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
            result += f"{elem} -> "
        return result[:-3]

    def insert_at_start(self, *elements):
        elements = elements[::-1]
        current = self.head
        for elem in elements:
            current = Node(elem, current)
        self.head = current
        return self

    def insert_at_end(self, *elements):
        current = self.get_last()
        if current == None:
            self.insert_at_start(*elements)
            return self

        for elem in elements:
            current.next = Node(elem)
            current = current.next
        return self

    def insert(self, index, *elements):
        current = self[index-1]
        if current == None or index == 0:
            self.insert_at_start(*elements)
            return self
        end = current.next
        for elem in elements:
            current.next = Node(elem)
            current = current.next
        current.next = end
        return self

    def reverse(self):
        previous = None
        next = None
        current = self.head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
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
                return self.head
        for elem in self:
            if ind == index:
                return elem
            ind += 1
        # return self.get_last()

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
        else:
            start.next = end
        return self

    def __contains__(self, element):
        for elem in self:
            if elem.value == element:
                return True
        return False

    def remove_entries(self, element, entries=1):
        previous = None
        for node in self:
            if node.value == element:
                if previous == None:
                    self.head = node.next
                else:
                    previous.next = node.next
                entries -= 1
                if entries == 0:
                    break
            else:
                previous = node
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
