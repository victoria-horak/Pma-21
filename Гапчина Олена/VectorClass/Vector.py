class Vector:
    def __init__(self, data):
        self.vector = data

    @staticmethod
    def read_from_file(file_name):
        vector = []
        f = open(file_name, 'r')
        split_read = f.read().split('\n')
        f.close()
        for row_iterator in range(0, len(split_read)):
            row_element = split_read[row_iterator]
            if row_element != '':
                column_elements = row_element.split(",")
                for column_iterator in range(0, len(column_elements)):
                    element = column_elements[column_iterator]
                    if element != '':
                        vector.append(int(element))
        return vector

    def get_vector(self):
        return self.vector

    def print(self):
        for iterator in range(len(self.vector)):
            print(self.vector[iterator], end=" ")

    def write_to_file(self, file_name):
        f = open(file_name, 'w')
        for row_iterator in range(len(self.vector)):
            f.write(str(self.vector[row_iterator]) + ' ')
        f.close()

    def add(self, other):
        result = []
        for i in range(len(self.vector)):
            result.append(0)
        for i in range(len(self.vector)):
            result[i] = (self.vector[i] + other.get_vector()[i])
        return result

    def subtract(self, other):
        result = []
        for i in range(len(self.vector)):
            result.append(0)
        for i in range(len(self.vector)):
            result[i] = (self.vector[i] - other.get_vector()[i])
        return result

    def multiply(self, other):
        result = []
        for i in range(len(self.vector)):
            result.append(0)
        for i in range(len(self.vector)):
            result[i] = self.vector[i] * other.get_vector()[i]
        return result

    def divide(self, other):
        result = []
        for i in range(len(self.vector)):
            result.append(0)
        for i in range(len(self.vector)):
            if other.get_vector()[i] == 0:
                raise DifferentSize("Can't divide by zero!")
            result[i] = self.vector[i] / other.get_vector()[i]
        return result
