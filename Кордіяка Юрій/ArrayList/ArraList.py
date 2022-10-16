from ExceptionsIsElement import ExceptionIsElementPresent


class ArrayList():
    def __init__(self, array):
        self.array = array

    def __getitem__(self, item):
        return self.array[item]

    def __len__(self):
        return len(self.array) - self.None_of_array()

    def insert(self, index, value):
        not_none = self.Not_none()
        if not_none < index:
            raise ExceptionIsElementPresent('element is not present')
        else:
            length = round(len(self.array) * 1.6)
            count_none = self.None_of_array()
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

    def None_of_array(self):
        count = 0
        for i in range(len(self.array)):
            if self.array[i] is None:
                count = count + 1
        return count

    def Not_none(self):
        count = 0
        for i in range(len(self.array)):
            if self.array[i] is not None:
                count = count + 1
        return count

    def __str__(self):
        new_array = []
        for i in range(len(self.array)):
            if self.array[i] is not None:
                new_array.append(self.array[i])
        return str(new_array)

    def clear_of_elements(self):
        return self.array.clear()

    def append_to_ArrayList(self, value):
        count_none = ArrayList.None_of_array(self)
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
        count_none = self.None_of_array()

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

    def pop_from_list(self, index):
        self.array.pop(index)
        return self.array

    def if_element_present(self, element):
        bool = False
        for i in range(len(self.array)):
            if self.array[i] == element:
                bool = True
                break
        return print(str(bool))

    def sotr_array(self):
        count_none = self.None_of_array()
        if count_none == 0:
            return self.array.sort()
        else:
            position_of_none = 0
            for i in range(len(self.array)):
                if self.array[i] is None:
                    position_of_none = i
                    break
            element_before = [self.array[element] for element in range(len(self.array)) if
                              position_of_none > element]
            element_before.sort()
            for i in range(len(element_before)):
                self.array[i] = element_before[i]
            return self.array
