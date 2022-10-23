class ArrayList:

    def __init__(self, *array_list):
        self.array_list = []
        for iterator in array_list:
            self.array_list.append(iterator)

    def get_iterator(self):
        return self.Iterator(self.array_list)

    def add_one_element(self, value):
        self.array_list.append(value)

    def add_more_element(self, *values):
        for iterator in values:
            self.array_list.append(iterator)

    def remove_one_element(self, value):
        self.array_list.remove(value)

    def remove_all_enter_element(self, value):
        for iterator in range(len(self.array_list) - 1, -1, -1):
            if self.array_list[iterator] == value:
                del self.array_list[iterator]

    def remove_last_enter_element(self, value):
        for iterator in range(len(self.array_list) - 1, -1, -1):
            if self.array_list[iterator] == value:
                del self.array_list[iterator]
                return

    def remove_more_element(self, *values):
        for iterator in values:
            self.array_list.remove(iterator)

    def remove_all_enter_elements(self, *values):
        for iterator in range(len(self.array_list) - 1, -1, -1):
            for jterator in values:
                if self.array_list[iterator] == jterator:
                    del self.array_list[iterator]
                    break

    def remove_last_enter_elements(self, *values):
        self.array_list.reverse()
        self.remove_more_element(*values)
        self.array_list.reverse()

    def __str__(self):
        return str(self.array_list)

    def read_from_file(self, file_name):
        with open(file_name, 'r') as file:
            file_lines = file.read().split("\n")
            row = []
            for line_index in range(0, len(file_lines)):
                file_line = file_lines[line_index]
                if file_line == '':
                    continue
                line_elements = file_line.split(" ")
                for element_index in range(0, len(line_elements)):
                    line_element = line_elements[element_index]
                    if line_element == '':
                        continue
                    number = int(line_element)
                    row.append(number)
            self.array_list += row

    class Iterator:
        def __init__(self, array_list):
            self.array_list = array_list
            self.index = 0

        def next(self):
            self.index += 1
            return self.array_list[self.index - 1]

        def has_next(self):
            return self.index < len(self.array_list)
