from IndexError import *


class ArrayList:
    def __init__(self, array):
        self.array = array

    def __getitem__(self, item):
        return self.array[item]

    def __len__(self):
        return len(self.array) - self.countNoneInArray()

    def __str__(self):
        new_array = []
        for i in range(len(self.array)):
            if self.array[i] is not None:
                new_array.append(self.array[i])
        return str(new_array)

    def countElements(self):
        count = 0
        for i in range(len(self.array)):
            if self.array[i] is not None:
                count = count + 1
        return count

    def countNoneInArray(self):
        count = 0
        for i in range(len(self.array)):
            if self.array[i] is None:
                count = count + 1
        return count

    def insertAtIndex(self, index, value):
        counter_not_none = self.countElements()
        if counter_not_none < index:
            raise IndexError("Index Error")
        else:
            length = round(len(self.array) * 1.6)
            count_none = self.countNoneInArray()
            element_after_index = [self.array[element] for element in range(len(self.array)) if element > index - 1]
            for i in range(len(self.array)):
                if i == index:
                    self.array[i] = value
            self.array = [self.array[element] for element in range(len(self.array)) if element < index + 1]
            if count_none == 0:
                new_array = [None] * length
                self.array += element_after_index
                for i in range(len(self.array)):
                    new_array[i] = self.array[i]
                self.array = new_array
                return new_array
            else:
                self.array += element_after_index
                self.array.pop(-1)
                return self.array

    def insertAtBegin(self, value):
        self.insertAtIndex(0, value)
        return self.array

    def insertFrom(self, index_from, value: list):
        if 0 <= index_from <= self.__len__():
            for index in range(len(self.array)):
                if index == index_from:
                    for j in range(len(value)):
                        self.insertAtIndex(index, value[j])
                        index += 1
        else:
            raise IndexError("Index Error")
        return self.array

    def insertAtEnd(self, value):
        count_none = ArrayList.countNoneInArray(self)
        length = round(len(self.array) * 1.6)
        if count_none == 0:
            new_array = [None] * length
            for i in range(len(self.array)):
                new_array[i] = self.array[i]
            for i in range(len(new_array)):
                if new_array[i] is None:
                    new_array[i] = value
                    break
            self.array = new_array
            return self.array
        elif count_none != 0:
            for i in range(len(self.array)):
                if self.array[i] is None:
                    self.array[i] = value
                    break
            return self.array

    def reverse(self):
        count_none = self.countNoneInArray()
        if count_none == 0:
            self.array = self.array[::-1]
            return self.array
        else:
            position_of_none = 0
            for i in range(len(self.array)):
                if self.array[i] is None:
                    position_of_none = i
                    break
            element_before_None = [self.array[element] for element in range(len(self.array)) if
                                   position_of_none > element]
            reverse_array = element_before_None[::-1]
            for i in range(len(reverse_array)):
                self.array[i] = reverse_array[i]
            return self.array

    def deleteAllArray(self):
        self.__init__([])

    def deleteAtIndex(self, index):
        if 0 < index <= self.__len__():
            self.array.pop(index)
            return self.array
        else:
            raise IndexError("Index Error")

    def deleteFromTo(self, index_from, index_to):
        if index_from > index_to:
            index_from, index_to = index_to, index_from
        if 0 < index_from <= self.__len__() and 0 < index_to <= self.__len__():
            for index in range(self.__len__()):
                if index == index_from:
                    for i in range(index_to - index_from):
                        self.deleteAtIndex(index)
            return self.array
        else:
            raise IndexError("Index Error")

    def elementPresent(self, element):
        flag = False
        for i in range(len(self.array)):
            if self.array[i] == element:
                flag = True
                break
        return print(str(flag))

    def sortArray(self):
        count_none = self.countNoneInArray()
        if count_none == 0:
            return self.array.sort()
        else:
            position_of_none = 0
            for i in range(len(self.array)):
                if self.array[i] is None:
                    position_of_none = i
                    break
            element_before_none = [self.array[element] for element in range(len(self.array))
                                   if position_of_none > element]
            element_before_none.sort()
            for i in range(len(element_before_none)):
                self.array[i] = element_before_none[i]
            return self.array
