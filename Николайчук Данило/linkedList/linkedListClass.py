class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        return str(self.data)


class linkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node(previous=self.head)
        self.head.next = self.tail

    def __str__(self):
        if self.head.data == None:
            return "[]"
        if self.tail.data == None:
            return "[" + str(self.head.data) + "]"
        if len(self) == 2:
            return "[" + str(self.head.data) + ", " + str(self.tail) + "]"
        out = "["
        curent = self.head
        for temp in range(len(self)):
            out += str(curent.data) + ", "
            curent = curent.next
        out = out[0:len(out) - 2]
        return out + "]"

    def __len__(self):
        if self.head.data == None:
            return 0
        if self.tail.data == None:
            return 1
        count = 1
        curent = self.head
        while curent != self.tail:
            count += 1
            curent = curent.next
        return count

    def printFromEnd(self):
        if self.head.data == None:
            print("[]")
            return
        if self.tail.data == None:
            print("[" + str(self.head.data) + "]")
            return
        curent = self.tail
        out = "["
        for temp in range(len(self)):
            out += (str(curent.data) + ", ")
            curent = curent.previous
        out = out[0:len(out) - 2]
        print(out + "]")

    def isEmpty(self):
        if self.head.data == None:
            return True
        return False

    def elementAt(self, index):
        try:
            if index < 0 or index > len(self):
                raise IndexError("index out of range(elementAt()).")
        except IndexError as exc:
            print("Error: ", str(exc))
            return
        curent = self.head
        iterator = 0
        while curent:
            if iterator == index:
                return curent
            curent = curent.next
            iterator += 1

    def emplace_back(self, *elements):
        for element in elements:
            if self.head.data == None:
                self.head.data = element
                continue
            if self.tail.data == None:
                self.tail.data = element
                continue
            newNode = Node(element, None, self.tail)
            self.tail.next = newNode
            self.tail = newNode

    def emplace_front(self, *elements):
        for element in elements:
            if self.head.data == None:
                self.head = Node(element, self.tail)
                self.tail.previous = self.head
                continue

            if self.tail.data == None:
                self.tail = self.head
            newNode = Node(element, self.head)
            self.head.previous = newNode
            self.head = newNode

    def emplace_in(self, index, *elements):
        for element in elements:
            try:
                if index < 0 or index > len(self):
                    raise IndexError("index out of range(emplace_in()).")
            except IndexError as exc:
                print("Error: ", str(exc))
                return
            curent = self.elementAt(index)
            if curent == self.head:
                self.emplace_front(element)
                continue
            if curent == self.tail:
                self.emplace_back(element)
                continue
            newNode = Node(element, curent, curent.previous)
            previous = curent.previous
            previous.next = newNode
            curent.previous = newNode
            curent = newNode

    def emplace_ListInBack(self, other):
        try:
            if other.head.data ==None:
                return
            if self.head == None:
                self.head = other.head
                self.tail = other.tail
                return
            if self.tail.data == None:
                self.tail.data = other.head.data
                self.head.next = self.tail
                self.tail.next = other.head.next
                self.tail = other.tail
                return
            self.tail.next = other.head
            self.tail = other.tail
        except AttributeError as exc:
            print("Error: you have entered incorect data,", str(exc))

    def emplace_ListFront(self, other):
        try:
            other.emplace_ListInBack(self)
            self.head = other.head
            self.tail = other.tail
        except AttributeError as exc:
            print("Error: you have entered incorect data,", str(exc))

    def emplace_ListInIndex(self, index, other):
        try:
            if index < 0 or index > len(self):
                raise IndexError("index out of range(emplace_ListInIndex()).")
        except IndexError as exc:
            print("Error: ", str(exc))
            return
        if index == 0:
            self.emplace_ListFront(other)
            return
        if index == (len(self) - 1):
            self.emplace_ListInBack(other)
            return
        if len(other) == 0:
            return
        if len(other) == 1:
            self.emplace_in(index, other.head.data)
            return

        other.tail.next = self.elementAt(index)
        other.head.previous = self.elementAt(index).previous
        previous = self.elementAt(index).previous
        self.elementAt(index).previous = other.tail
        previous.next = other.head

    def pop_back(self, number=1):
        for iterator in range(number):
            if self.head.data == None:
                print("No date in list.")
                return
            if self.tail.data == None:
                self.clear()
                print("List is empty now.")
                return
            if self.tail.previous == self.head:
                self.tail.data = None
                continue
            previous = self.tail.previous
            previous.next = None
            self.tail = previous

    def pop_front(self, number=1):
        for iterator in range(number):
            if self.head.data == None:
                print("No date in list.")
                return
            if self.head.next == self.tail:
                self.head = self.tail
                self.tail = Node(previous=self.head)
                continue
            if self.tail.data == None:
                self.clear()
                print("List is empty now.")
                return
            second = self.head.next
            second.previous = None
            self.head = second

    def removeIndex(self, index):
        try:
            if index < 0 or index > len(self):
                raise IndexError("index out of range(removeIndex()).")
        except IndexError as exc:
            print("Error: ", str(exc))
            return
        curent = self.elementAt(index)
        if curent == self.tail:
            self.pop_back()
            return
        if curent == self.head:
            self.pop_front()
            return
        previous = curent.previous
        previous.next = curent.next
        next = curent.next
        next.previous = curent.previous

    def removeFromTo(self, startIndex, endIndex):
        try:
            if startIndex < 0 or startIndex > len(self) or endIndex < 0 or endIndex > len(self):
                raise IndexError("index out of range(removeFromTo()).")
        except IndexError as exc:
            print("Error: ", str(exc))
            return
        if startIndex > endIndex:
            (startIndex, endIndex) = (endIndex, startIndex)
        if startIndex == self.head and endIndex == self.tail:
            self.clear()
            return
        if startIndex == 0:
            self.elementAt(endIndex).previous = self.head
            self.head = self.elementAt(endIndex)
            return
        if endIndex == len(self) - 1:
            self.elementAt(startIndex).next = self.tail
            self.tail = self.elementAt(startIndex)
            return
        self.elementAt(endIndex).previous = self.elementAt(startIndex)
        self.elementAt(startIndex).next = self.elementAt(endIndex)

    def removeFirstEntery(self, *elements):
        for element in elements:
            curent = self.head
            iterator = 0
            while curent.next != None:
                if curent.data == element:
                    self.removeIndex(iterator)
                    break
                iterator += 1
                curent = curent.next

    def removeAllEnteries(self, *elements):
        for element in elements:
            curent = self.head
            iterator = 0
            for temp in range(0, len(self)):
                if curent.data == element:
                    self.removeIndex(iterator)
                else:
                    iterator += 1
                curent = curent.next

    def seachBool(self, element):
        curent = self.head
        while curent:
            if curent.data == element:
                return True
            curent = curent.next
        return False

    def searchPlace(self, element):
        curent = self.head
        iterator = 0
        while curent:
            if curent.data == element:
                return iterator
            curent = curent.next
            iterator += 1
        return -1

    def reverse(self):
        if len(self) < 2:
            return
        newList = linkedList()
        curent = self.head
        for temp in range(len(self)):
            newList.emplace_front(curent.data)
            curent = curent.next
        self.head = newList.head
        self.tail = newList.tail

    def swap(self, firstIndex, secondIndex):
        try:
            if firstIndex < 0 or firstIndex > len(self) or secondIndex < 0 or secondIndex > len(self):
                raise IndexError("index out of range(swap()).")
        except IndexError as exc:
            print("Error: ", str(exc))
            return
        if firstIndex == secondIndex:
            return
        (self.elementAt(firstIndex).data, self.elementAt(secondIndex).data) = \
            (self.elementAt(secondIndex).data, self.elementAt(firstIndex).data)

    def sort(self):
        if len(self) < 2:
            return

        for outIterator in range(len(self)):
            curent = self.elementAt(outIterator)
            minEl = curent.data
            minIterator = outIterator
            for iterator in range(outIterator, len(self)):
                try:
                    if curent.data <= minEl:
                        minEl = curent.data
                        minIterator = iterator
                except TypeError as exc:
                    print("Error: ", str(exc))
                    return
                curent = curent.next
            self.swap(outIterator, minIterator)

    def clear(self):
        newList = linkedList()
        self.head = newList.head
        self.tail = newList.tail
