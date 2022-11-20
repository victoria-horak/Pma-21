from Invalid import Invalid


class Array:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.array = array
        self.resize()

    def __str__(self):
        temp = ""
        for i in range(self.length()):
            temp += str(self.array[i]) + ","
        temp = temp[:-1]
        return temp

    def size(self):
        return len(self.array)

    def length(self):
        count = 0
        for i in range(self.size()):
            if self.array[i] is not None:
                count += 1
        return count

    def complete(self):
        return self.array[self.size() - 1] is not None

    def resize(self):
        temp = [None] * round(len(self.array) * 1.5 + 1)
        for i in range(len(self.array)):
            temp[i] = self.array[i]
        self.array = temp

    def addElements(self, *values):
        for value in values:
            if self.complete():
                self.resize()
            self.array[self.length()] = value

    def addElementByIndex(self, index, value):
        if self.length() >= index >= 0:
            if self.complete():
                self.resize()
            for i in range(self.length() - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]
            self.array[index] = value
        else:
            raise Invalid("Incorrect value")

    def deleteLastElement(self):
        temp = Array()
        for i in range(0, self.length() - 1):
            temp.addElements(self.array[i])
        self.array = temp.array
        temp.__init__()

    def deleteOneInsertion(self, *values):
        temp = Array()
        for value in values:
            flag = 0
            for i in range(self.size()):
                if self.array[i] == value and flag == 0:
                    flag = 1
                else:
                    temp.addElements(self.array[i])
            self.array = temp.array
            temp.__init__()

    def deleteAllSpecificElements(self, *values):
        temp = Array()
        for value in values:
            for i in range(self.size()):
                if self.array[i] != value:
                    temp.addElements(self.array[i])
            self.array = temp.array
            temp.__init__()

    def deleteByIndex(self, index):
        if self.length() > index >= 0:
            temp = Array()
            for i in range(self.size()):
                if i != index:
                    temp.addElements(self.array[i])
            self.array = temp.array
            temp.__init__()
        else:
            raise Invalid("Incorrect value")
