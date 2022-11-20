class ArrayList:

    def __init__(self, array=[]):
        self.array = array
        self.increaseCapacity()

    def __str__(self):
        if self.length() == 0:
            return "[]"
        result = "["
        for iterator in range(self.length()):
            result += str(self.array[iterator]) + ", "
        result = result[0:len(result) - 2]
        return result + "]"

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

    def at(self, index):
        try:
            if index >= self.length() or index < 0:
                raise IndexError
            for i in range(self.length()):
                if i == index:
                    return self.array[i]
        except IndexError:
            print("out of range")

    def increaseCapacity(self):
        tempArray = [None] * round(len(self.array) * 1.5 + 1)
        for i in range(len(self.array)):
            tempArray[i] = self.array[i]
        self.array = tempArray

    def append(self, *values):
        for value in values:
            if self.isFull():
                self.increaseCapacity()
            self.array[self.length()] = value

    def eraseAll(self, *values):
        tempArray = ArrayList()
        for value in values:
            if tempArray.isFull():
                tempArray.increaseCapacity()
            for i in range(self.capacity()):
                if self.array[i] != value:
                    tempArray.append(self.array[i])
            self.array = tempArray.array
            tempArray.__init__()

    def eraseFirst(self, *values):
        tempArray = ArrayList()
        for value in values:
            flag = 0
            if tempArray.isFull():
                tempArray.increaseCapacity()
            for i in range(self.capacity()):
                if self.array[i] == value and flag == 0:
                    flag += 1
                else:
                    tempArray.append(self.array[i])
            self.array = tempArray.array
            tempArray.__init__()

    def popFront(self, index):
        try:
            if index > self.length() or index < 0:
                raise IndexError
            tempArray = ArrayList()
            for i in range(index, self.capacity()):
                if tempArray.isFull():
                    tempArray.increaseCapacity()
                element = self.array[i]
                tempArray.append(element)
            self.array = tempArray.array
        except IndexError:
            print("out of range")

    def popBack(self, index):
        try:
            if index > self.length() or index < 0:
                raise IndexError
            tempArray = ArrayList()
            for i in range(0, self.capacity() - index):
                if tempArray.isFull():
                    tempArray.increaseCapacity()
                tempArray.append(self.array[i])
            self.array = tempArray.array
        except IndexError:
            print("out of range")

