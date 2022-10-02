class Matrix:

    def __init__(self, file_name):
        if isinstance(file_name, list):
            self.matrix = file_name
        else:
            self.matrix = Matrix.read_matrix(self, file_name)

    def get_row(self, iterator):
        return self.matrix[iterator]

    def get_matrix(self):
        return self.matrix

    def get_item(self, kterator, jterator):
        return self.matrix[kterator][jterator]

    @staticmethod
    def read_matrix(self, file_name):
        try:
            file = open(file_name, 'r')
            file_lines = file.read().split("\n")
        finally:
            file.close()
        matrix = []
        for line_index in range(0, len(file_lines)):
            file_line = file_lines[line_index]
            if file_line == '':
                continue
            line_elements = file_line.split(" ")
            row = []
            for element_index in range(0, len(line_elements)):
                line_element = line_elements[element_index]
                if line_element == '':
                    continue
                number = float(line_element)
                row.append(number)
            matrix.append(row)

        return matrix

    @staticmethod
    def get_read_string_matrix(matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    def __str__(self):
        return Matrix.get_read_string_matrix(self.matrix)

    def adding(self, second_matrix):
        results = []
        for iterator in range(0, len(self.matrix)):
            new_matrix = []
            for jterator in range(0, len(self.matrix[0])):
                result = float(self.matrix[iterator][jterator]) + float(second_matrix.matrix[iterator][jterator])
                new_matrix.append(result)
            results.append(new_matrix)
        return results

    def __add__(self, other_matrix):
        if isinstance(other_matrix, Matrix):
            return self.adding(other_matrix)

    def sub(self, second_matrix):
        results = []
        for iterator in range(0, len(self.matrix)):
            new_matrix = []
            for jterator in range(0, len(self.matrix[0])):
                result = float(self.matrix[iterator][jterator]) - float(second_matrix.matrix[iterator][jterator])
                new_matrix.append(result)
            results.append(new_matrix)
        return results

    def __sub__(self, other_matrix):
        if isinstance(other_matrix, Matrix):
            return self.sub(other_matrix)

    def multiply(self, second_matrix):
        result_multi_matrix = [[0 for jterator in range(len(second_matrix.get_row(iterator)))] for iterator in
                               range(len(self.matrix))]
        for iterator in range(len(self.matrix)):
            for jterator in range(len(second_matrix.get_row(iterator))):
                for kterator in range(len(second_matrix.get_matrix())):
                    result_multi_matrix[iterator][jterator] += self.matrix[iterator][kterator] * second_matrix.get_item(
                        kterator, jterator)
        return Matrix(result_multi_matrix)

    def __mul__(self, other_matrix):
        if isinstance(other_matrix, Matrix):
            return self.multiply(other_matrix)

    def write_matrix_in_file(self):
        try:
            with open("sources\\resultMatrix.txt", "a+") as matrix_file:
                matrix_file.write("\n")
                for row in self.matrix:
                    for column in row:
                        matrix_file.write(str(column))
                        matrix_file.write(" ")
                    matrix_file.write("\n")
        finally:
            matrix_file.close()
