class ArrayList:

    def __init__(self, *array_list):
        self.array_list = []
        for i in array_list:
            self.array_list.append(i)

    def read_from_file(self, file_name):
        row = []
        with open(file_name, 'r') as file:
            lines = file.read().split("\n")
            for line_index in range(0, len(lines)):
                line = lines[line_index]
                if line == '':
                    continue
                elements_on_line = line.split(" ")
                for index_of_element in range(0, len(elements_on_line)):
                    element_on_line = elements_on_line[index_of_element]
                    if element_on_line == '':
                        continue
                    num = int(element_on_line)
                    row.append(num)
            self.array_list += row

    def __str__(self):
        return str(self.array_list)

    def append_one(self, value):
        self.array_list.append(value)

    def append_more(self, *values):
        for iterator in values:
            self.array_list.append(iterator)

    def pop_one(self, value):
        self.array_list.remove(value)

    def pop_all_entered(self, value):
        for iterator in range(len(self.array_list) - 1, -1, -1):
            if self.array_list[iterator] == value:
                del self.array_list[iterator]

    def pop_last_entered(self, value):
        for iterator in range(len(self.array_list) - 1, -1, -1):
            if self.array_list[iterator] == value:
                del self.array_list[iterator]
                return

    def pop_more(self, *values):
        for iterator in values:
            self.array_list.remove(iterator)

    def pop_all_entered_elements(self, *values):
        for iterator in range(len(self.array_list) - 1, -1, -1):
            for jterator in values:
                if self.array_list[iterator] == jterator:
                    del self.array_list[iterator]
                    break

    def pop_last_entered_elements(self, *values):
        self.array_list.reverse()
        self.pop_more(*values)
        self.array_list.reverse()

    def clear(self):
        del self.array_list

    def size(self):
        new_size = int(1.5 * len(self.array_list) + 1)
        for i in range(0, new_size - len(self.array_list)):
            self.array_list.append(0)
        return self.array_list
