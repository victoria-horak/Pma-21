from typing import TypeVar, Generic
from InvalidIndexException import InvalidIndexException

T = TypeVar('T')

class ArrayList(Generic[T]):
    def __init__(self):
        self.array = ArrayList.make_array()
        self.length = 0

    def make_array():
        return [0 for i in range(10000)]

    def add(self, item: T):
        self.array[self.length] = item
        self.length += 1

    def __getitem__(self, index):
        if (index >= self.length or index < 0):
            raise InvalidIndexException("Index is out of bounds")
        return self.array[index]

    def get(self, index):
        return self.__getitem__(index)

    def size(self):
        return self.length

    def sort(self):
        for i in range(self.length):
            for j in range(i + 1, self.length):
                if (self.array[i] > self.array[j]):
                    self.array[i], self.array[j] = self.array[j], self.array[i]

    def __str__(self):
        result = '['
        for i in range(self.length):
            result += str(self.array[i]) + ','
        if (self.length):
            result = result[:-1]
        result += ']'
        return result

    def pop(self):
        self.length -= 1
        self.array[self.length] = 0

    def remove_at(self, index):
        if (index >= self.length or index < 0):
            raise InvalidIndexException("Index is out of bounds")
        new_array = ArrayList()
        for i in range(index):
            new_array.add(self.array[i])
        for i in range(index + 1, self.length):
            new_array.add(self.array[i])
        return new_array

    def insert(self, index, value: T):
        if (index < 0):
            raise InvalidIndexException("Index is out of bounds")
        new_array = ArrayList()
        for i in range(self.length):
            if (i == index):
                new_array.add(value)
            new_array.add(self.array[i])
        return new_array
    
    def replace(self, index, value: T):
        if (index < 0 or index >= self.length):
            raise InvalidIndexException("Index is out of bounds")
        self.array[index] = value
        return self
    
    def clear(self):
        self.length = 0
        self.array = ArrayList.make_array()
    
    def remove(self, item: T):
        new_array = ArrayList()
        for i in range(self.length):
            if self.array[i] != item:
                new_array.add(self.array[i])
        return new_array

    def reverse(self):
        new_array = ArrayList()
        for i in reversed(range(self.length)):
            new_array.add(self.array[i])
        return new_array
