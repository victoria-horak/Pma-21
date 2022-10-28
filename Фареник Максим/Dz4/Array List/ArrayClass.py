from IndexException import IndexException


class ArrayList:
    def __init__(self, array=[]):
        self.array = array
        self.resize()

    def __str__(self):
        temp = ""
        for i in range(self.length()):
            temp += str(self.array[i]) + ","
        temp = temp[:-1]
        return "[" + temp + "]"

    def capacity(self):
        return len(self.array)

    def length(self):
        count = 0
        for i in range(self.capacity()):
            if self.array[i] is not None:
                count += 1
        return count

    def str(self):
        return str(self.array)

    def isFull(self):
        return self.array[self.capacity() - 1] is not None

    def clear(self):
        self.__init__()

    def resize(self):
        temp = [None] * round(len(self.array) * 1.5 + 1)
        for i in range(len(self.array)):
            temp[i] = self.array[i]
        self.array = temp

    def append(self, *values):
        for value in values:
            if self.isFull():
                self.resize()
            self.array[self.length()] = value

    def insert(self, index, value):
        if index <= self.length() and index >= 0:
            if self.isFull():
                self.resize()
            for i in range(self.length() - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]
            self.array[index] = value
        else:
            raise IndexException("INCORRECT INDEX!!!!!")

    def pop(self):
        temp = ArrayList()
        for i in range(0, self.length() - 1):
                temp.append(self.array[i])
        self.array = temp.array
        temp.__init__()


    def removeAll(self, *values):
        temp = ArrayList()
        for value in values:
            for i in range(self.capacity()):
                if self.array[i] != value:
                    temp.append(self.array[i])
            self.array = temp.array
            temp.__init__()

    def removeByIndex(self, index):
        if index < self.length() and index >= 0:
            temp = ArrayList()
            for i in range(self.capacity()):
                if i != index:
                    temp.append(self.array[i])
            self.array = temp.array
            temp.__init__()
        else:
            raise IndexException("INCORRECT INDEX!!!!!")

    def removeOneInsertion(self, *values):
        temp = ArrayList()
        for value in values:
            flag = 0
            for i in range(self.capacity()):
                if self.array[i] == value and flag == 0:
                    flag = 1
                else:
                    temp.append(self.array[i])
            self.array = temp.array
            temp.__init__()

