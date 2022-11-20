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
            file_name = open(file_name, 'r')
            file_lines = file_name.read().split("\n")
        finally:
            file_name.close()
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
        if len(self.matrix) == len(second_matrix.get_matrix()) and len(self.matrix[0]) == len(
                second_matrix.get_matrix()[0]):
            results = []
            for iterator in range(0, len(self.matrix)):
                new_matrix = []
                for jterator in range(0, len(self.matrix[0])):
                    result = float(self.matrix[iterator][jterator]) + float(
                        second_matrix.matrix[iterator][jterator])
                    new_matrix.append(result)
                results.append(new_matrix)
            return Matrix(results)
        else:
            with open("sources\\resultMatrix.txt", "a+") as matrix_file:
                matrix_file.write("We cannot add this matrix")
            return Matrix([])

    def __add__(self, other_matrix):
        if isinstance(other_matrix, Matrix):
            return self.adding(other_matrix)

    def sub(self, second_matrix):
        if len(self.matrix) == len(second_matrix.get_matrix()) and len(self.matrix[0]) == len(
                second_matrix.get_matrix()[0]):
            results = []
            for iterator in range(0, len(self.matrix)):
                new_matrix = []
                for jterator in range(0, len(self.matrix[0])):
                    result = float(self.matrix[iterator][jterator]) - float(
                        second_matrix.matrix[iterator][jterator])
                    new_matrix.append(result)
                results.append(new_matrix)
            return Matrix(results)
        else:
            with open("sources\\resultMatrix.txt", "a+") as matrix_file:
                matrix_file.write("We cannot sub this matrix")
            return Matrix([])

    def __sub__(self, other_matrix):
        if isinstance(other_matrix, Matrix):
            return self.sub(other_matrix)

    def multiply(self, second_matrix):
        second_matrix = second_matrix.get_matrix()
        min_len = min(len(self.matrix), len(second_matrix))
        max_len = max(len(self.matrix), len(second_matrix))
        result_multi_matrix = []
        for iterator in range(max_len):
            row = []
            for jterator in range(max_len):
                suma = 0
                for kterator in range(min_len):
                    if len(self.matrix) < len(second_matrix):
                        suma += self.matrix[kterator][iterator] * second_matrix[jterator][kterator]
                    else:
                        suma += self.matrix[iterator][kterator] * second_matrix[kterator][jterator]
                row.append(suma)
            result_multi_matrix.append(row)
        return Matrix(result_multi_matrix)

    def __mul__(self, other_matrix):
        if isinstance(other_matrix, Matrix):
            return self.multiply(other_matrix)

    def division(self, second_matrix):
        second_matrix = second_matrix.get_matrix()
        if len(second_matrix) != len(second_matrix[0]) or len(self.matrix) != len(second_matrix[0]):
            print("No work")
            return Matrix([])
        if len(second_matrix) == 2:
            d = self.determinant_matrix2x2(second_matrix)
            if d == 0:
                print("we cannot found this answer")
                return Matrix([])
            second_matrix = self.inversion_matrix2x2(second_matrix)
            return self.multiply(Matrix(second_matrix))

        if len(second_matrix) == 3:
            d = self.determinant_matrix3x3(second_matrix)
            if d == 0:
                print("we cannot found this answer")
                return Matrix([])
            second_matrix = self.inversion_matrix3x3(second_matrix)
            return self.multiply(Matrix(second_matrix))
        if len(second_matrix) == 1:
            print("we cannot found this answer")
            return Matrix([])
        if len(second_matrix) > 3:
            print("we cannot found this answer")
            return Matrix([])
    @staticmethod
    def determinant_matrix3x3(matrix):
        determinant = 0
        for iterator in range(3):
            positive_number = 1
            negative_number = 1
            for jterator in range(3):
                positive_number *= matrix[jterator][(iterator + jterator) % 3]
                negative_number *= matrix[jterator][(iterator - jterator) % 3]
            determinant += (positive_number - negative_number)
        return determinant

    def inversion_matrix3x3(self, other):
        new_matrix = [3 * [None] for _iterator in range(3)]
        determinant_matrix3x3 = self.determinant_matrix3x3(other)
        print("Determinant", determinant_matrix3x3)
        print("Element Inversion Matrix3x3:", end=" ")
        for _iterator in range(3):
            for _jterator in range(3):
                adj = [[n for _iterator_iterator, n in enumerate(row) if _iterator_iterator != _iterator]
                       for _jterator_jterator, row in enumerate(other) if _jterator_jterator != _jterator]
                determinant_matrix2x2 = self.determinant_matrix2x2(adj)
                signum = (-1) ** (_iterator + _jterator)
                element_inverse_matrix3x3 = signum * determinant_matrix2x2 / determinant_matrix3x3
                print(signum * determinant_matrix2x2, end=" ")
                new_matrix[_iterator][_jterator] = round(element_inverse_matrix3x3, 3)
        print("\ninversion matrix mult in 1/determinant", end=" ")
        print(new_matrix)
        return new_matrix

    @staticmethod
    def determinant_matrix2x2(matrix):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    def inversion_matrix2x2(self, matrix):
        determinant = self.determinant_matrix2x2(matrix)
        return [[matrix[1][1] / determinant, -matrix[0][1] / determinant],
                [-matrix[1][0] / determinant, matrix[0][0] / determinant]]

    def __truediv__(self, other_matrix):
        if isinstance(other_matrix, Matrix):
            return self.division(other_matrix)

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
