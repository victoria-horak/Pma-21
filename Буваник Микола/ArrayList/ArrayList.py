from BadIndexException import BadIndexExeption


class ArrayList:
    def __init__(self, array=None):
        if array is None:
            self.__array = []
        else:
            self.__array = array

    def __str__(self):
        return str(self.arrayWithoutNone())

    def clear(self):
        return self.__array.clear()

    def arrayWithoutNone(self):
        array = []
        for iterator in self.__array:
            if iterator is not None:
                array.append(iterator)
        return array

    def ArrayFull(self):
        for iterator in self.__array:
            if iterator is None:
                return False
        return True

    def NewArrayCreator(self):
        newArray = [None] * round(len(self.__array) * 1.5 + 1)
        for iterator in range(len(self.__array)):
            newArray[iterator] = self.__array[iterator]
        self.__array = newArray

    def append(self, element):
        if type(element) is list:
            for iterator in element:
                if self.ArrayFull():
                    self.NewArrayCreator()
                self.__array[len(self.arrayWithoutNone())] = iterator
        else:
            if self.ArrayFull():
                self.NewArrayCreator()
            self.__array[len(self.arrayWithoutNone())] = element

    def pop(self, index=None):
        if index is None:
            self.__array.append(None)
            return self.__array.pop(len(self.arrayWithoutNone()) - 1)
        else:
            if type(index) is list:
                for iterator in index:
                    if iterator < len(self.arrayWithoutNone()):
                        self.__array.append(None)
                        self.__array.pop(iterator)
                    else:
                        raise BadIndexExeption("Index Error")
            else:
                if index <= len(self.arrayWithoutNone()) - 1:
                    self.__array.append(None)
                    return self.__array.pop(index)
                else:
                    raise BadIndexExeption("Index Error")

    def remove(self, value):
        if type(value) is list:
            for iterator in value:
                while iterator in self.__array:
                    self.__array.remove(iterator)
                    self.__array.append(None)
        else:
            while value in self.__array:
                self.__array.remove(value)
                self.__array.append(None)
        return self.__array

    def sort(self, key=None):
        array = self.arrayWithoutNone()
        if key is None:
            array.sort()
        else:
            array.sort(key=key)
        array += [None] * (len(self.__array) - len(self.arrayWithoutNone()))
        self.__array = array
        return self.__array

    def insert(self, element, index):
        if self.ArrayFull():
            self.NewArrayCreator()
        if type(element) is list:
            for iterator in reversed(element):
                if self.ArrayFull():
                    self.NewArrayCreator()
                if index <= len(self.arrayWithoutNone()):
                    self.__array.insert(index, iterator)
                    self.__array.pop()
                else:
                    raise BadIndexExeption("Index Error")
        else:
            if self.ArrayFull():
                self.NewArrayCreator()
            if index <= len(self.arrayWithoutNone()):
                self.__array.insert(index, element)
                self.__array.pop()
            else:
                raise BadIndexExeption("Index Error")

    def __len__(self):
        return len(self.__array)

    def __getitem__(self, item):
        return self.__array[item]
