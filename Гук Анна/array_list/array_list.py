import ctypes
from exception import Exception_array




class ArrayList:
    def __init__(self):
        self.len = 0
        self.size = 1
        self.array = self.array_full(self.size)


    def array_full(self, volume):
        return (volume * ctypes.py_object)()




    def __len__(self):
        return self.len

    def __getitem__(self, index):
        if self.len >= index >= 0:
            return self.array[index]
        else:
            raise Exception_array("!!!index error!!!")

    def append(self, item):
        if self.len == self.size:
            self.resize(2 * self.size)
        self.array[self.len] = item
        self.len += 1

    def resize(self, second_volume):
        second_array = self.array_full(second_volume)
        self.size = second_volume
        for i in range(self.len):
            second_array[i] = self.array[i]
        self.array = second_array


    def insert(self, index, value):
        if self.len >= index >= 0:
            if self.len == self.size:
                self.resize(2 * self.size)
            for i in range(self.len - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]
            self.array[index] = value
            self.len += 1
        else:
            raise Exception_array("!!!index error!!!")


    def remove_element_by_index(self, index):
        if self.len >= index >= 0:
            for i in range(index, self.len - 1):
                self.array[i] = self.array[i + 1]
            self.len -= 1
        else:
            raise Exception_array("!!!index error!!!")

    def remove_element(self, value):
        flag = 0
        for i in range(self.len):
            if self.array[i] == value:
                flag = 1
                for j in range(i, self.len - 1):
                    self.array[j] = self.array[j + 1]
                self.len -= 1
                break
        if flag == 0:
            print("Value isn't found")

    def pop(self):
        self.len -= 1

    def clear(self):
        self.len = 0
        self.size = 1

    def next(self):
        for i in range(self.len):
           return self.array[i+1]

    def find(self, item):
        flag = 0
        for i in range(self.len):
            if self.array[i] == item:
                flag = 1
                break
        if flag == 1:
            return i
        else:
            print("there is no such element")

    def __str__(self):
        temp = ""
        for i in range(self.len):
            temp += str(self.array[i]) + ";"
        temp = temp[:-1]
        return "[" + temp + "]"
