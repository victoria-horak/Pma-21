import ctypes
from IndexException import IndexException


class ArrayList:
    def __init__(self):
        self.n = 0
        self.size = 1
        self.arrayA = self.makeArray(self.size)

    def makeArray(self, capacity):
        return (capacity * ctypes.py_object)()

    def append(self, item):
        if self.n == self.size:
            self.resize(2 * self.size)
        self.arrayA[self.n] = item
        self.n += 1

    def resize(self, new_capacity):
        arrayB = self.makeArray(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            arrayB[i] = self.arrayA[i]
        self.arrayA = arrayB

    def __str__(self):
        temp = ""
        for i in range(self.n):
            temp += str(self.arrayA[i]) + ","
        temp = temp[:-1]
        return "[" + temp + "]"

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if index <= self.n and index >= 0:
            return self.arrayA[index]
        else:
            raise IndexException("INCORRECT INDEX!!!!")

    def insert(self, index, value):
        if index <= self.n and index >= 0:
            if self.n == self.size:
                self.resize(2 * self.size)
            for i in range(self.n - 1, index - 1, -1):
                self.arrayA[i + 1] = self.arrayA[i]
            self.arrayA[index] = value
            self.n += 1
        else:
            raise IndexException("INCORRECT INDEX!!!!!")

    def removeByIndex(self, index):
        if index <= self.n and index >= 0:
            for i in range(index, self.n - 1):
                self.arrayA[i] = self.arrayA[i + 1]
            self.n -= 1
        else:
            raise IndexException("INCORRECT INDEX!!!!!")

    def remove(self, value):
        flag = 0
        for i in range(self.n):
            if self.arrayA[i] == value:
                flag = 1
                for j in range(i, self.n - 1):
                    self.arrayA[j] = self.arrayA[j + 1]
                self.n -= 1
                break
        if flag == 0:
            print("Value isn't found")

    def pop(self):
        self.n -= 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        flag = 0
        for i in range(self.n):
            if self.arrayA[i] == item:
                flag = 1
                break
        if flag == 1:
            return i
        else:
            raise IndexException("Item isn't found")
