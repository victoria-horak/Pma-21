class ArrayList:
    def __init__(self, arr=None):
        if arr == None:
            self.list = []
            self.length = 0
        else:
            self.list = arr
            self.length = len(arr)
        self.arrAddSpace()

    def __str__(self):
        if self.length == 0:
            return "[]"
        out = "["
        for iterator in range(0, self.length - 1):
            out += str(self.list[iterator]) + ", "
        out += str(self.list[self.length - 1]) + "]"
        return out

    def arrAddSpace(self, sizeOfIncrease=1.5):
        newArr = ([None] * int(len(self.list) * sizeOfIncrease + 1))
        for iterator in range(0, len(self.list)):
            newArr[iterator] = self.list[iterator]
        self.list = newArr

    def isArrFull(self):
        if self.list[len(self.list) - 1] == None:
            return False
        return True

    def __len__(self):
        return self.length

    def reservedSize(self):
        return len(self.list)

    def append(self, *elements):
        for element in elements:
            if self.isArrFull():
                self.arrAddSpace()
            self.list[self.length] = element
            self.length += 1

    def extend(self, otherList):
        self.arrAddSpace(len(otherList.list) / len(self.list))
        for iterator in range(0, otherList.length):
            if self.isArrFull():
                self.arrAddSpace()
            self.list[self.length] = otherList.list[iterator]
            self.length += 1

    def insert(self, index, *elements):
        if index > self.length:
            index = self.length
        for element in elements:
            if self.isArrFull():
                self.arrAddSpace()
            try:
                temp = self.list[index]
                self.list[index] = element
                for iterator in range(index + 1, self.length + 1):
                    tempBefore = self.list[iterator]
                    self.list[iterator] = temp
                    temp = tempBefore
            except IndexError as exc:
                print("Error: " + str(exc))
                exit(1)
            self.length += 1
            index += 1

    def fillWithNone(self, index=0):
        try:
            for iterator in range(index, len(self.list)):
                self.list[iterator] = None
        except IndexError as exc:
            print("Error: " + str(exc))
            exit(1)

    def remove(self, *elements):
        for element in elements:
            newArr = ([None] * len(self.list))
            newIterator = 0
            for iterator in range(0, self.length):
                if self.list[iterator] != element:
                    newArr[newIterator] = self.list[iterator]
                    newIterator += 1
                else:
                    self.length -= 1
            self.list = newArr

    def removeFirst(self, *elements):
        for element in elements:
            for iterator in range(0 , self.length):
                if element == self.list[iterator]:
                    self.pop(iterator)
                    break

    def pop(self, index=-1):
        if index < 0:
            index = self.length - 1
        indexValue = 0
        try:
            indexValue = self.list[index]
            for iterator in range(index, self.length - 1):
                self.list[iterator] = self.list[iterator + 1]
            self.length -= 1
        except IndexError as exc:
            print("Error: " + str(exc))
            exit(1)
        self.fillWithNone(self.length)
        return indexValue

    def index(self, element, startIterator=0, endIterator=-1):
        if endIterator < 0:
            endIterator = self.length
        for iterator in range(startIterator, endIterator):
            if self.list[iterator] == element:
                return iterator
        return -1

    def count(self, element):
        amount = 0
        for listElement in range(0, self.length):
            if self.list[listElement] == element:
                amount += 1
        return amount

    def sort(self):
        for iterator in range(0, self.length - 1):
            minJ = iterator
            for nestedIterator in range(iterator, self.length):
                try:
                    if self.list[nestedIterator] < self.list[minJ]:
                        minJ = nestedIterator
                except TypeError as exc:
                    print("Error: " + str(exc))
                    exit(1)
                except:
                    print("Error.")
            self.list[iterator], self.list[minJ] = self.list[minJ], self.list[iterator]

    def reverse(self):
        newArr = ([None] * len(self.list))
        newArrIterator = 0
        for iterator in range(self.length - 1, -1, -1):
            newArr[newArrIterator] = self.list[iterator]
            newArrIterator += 1
        self.list = newArr

    def copy(self):
        copyArr = ([None] * len(self.list))
        for iterator in range(self.length):
            copyArr[iterator] = self.list[iterator]
        newList = ArrayList(copyArr)
        newList.length = self.length
        return newList

    def clear(self):
        self.fillWithNone()
        self.length = 0
