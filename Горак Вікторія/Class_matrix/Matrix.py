from Exception import *


class Matrix:
    def __init__(self, row, column):
        self.matrix = [[0 * column] * row]

    def set_matrix(self, matrix_first):
        self.matrix = matrix_first
        return self.matrix

    def read_matrix(self, name_of_file):
        file = open(name_of_file, 'r')
        matrix_first = []
        read_text = file.read().split('\n')
        for i in range(len(read_text)):
            rows = read_text[i].split()
            n = 0
            for j in range(len(rows)):
                if (rows[j].isdigit()):
                    n += 1
            if (n != 0):
                matrix_first.append(" ".join(rows))
        file.close()

        self.matrix = [list(map(int, row.split())) for row in matrix_first]

    def add_matrix(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        matrix_result = Matrix(len(self.matrix), len(self.matrix[0]))
        matrix_add = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix_add[i][j] = self.matrix[i][j] + second.matrix[i][j]
        matrix_result.set_matrix(matrix_add)
        return matrix_result

    def __add__(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes \n")
        matrix_result = Matrix(len(self.matrix), len(self.matrix[0]))
        matrix_add = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix_add[i][j] = self.matrix[i][j] + second.matrix[i][j]
        matrix_result.set_matrix(matrix_add)
        return matrix_result

    def sub_matrix(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        matrix_result = Matrix(len(self.matrix), len(self.matrix[0]))
        matrix_sub = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix_sub[i][j] = self.matrix[i][j] - second.matrix[i][j]
        matrix_result.set_matrix(matrix_sub)
        return matrix_result

    def __sub__(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        matrix_result = Matrix(len(self.matrix), len(self.matrix[0]))
        matrix_sub = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix_sub[i][j] = self.matrix[i][j] - second.matrix[i][j]
        matrix_result.set_matrix(matrix_sub)
        return matrix_result

    def mult_matrix(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        matrix_result = Matrix(len(self.matrix), len(self.matrix[0]))
        matrix_mult = [[0] * len(second.matrix[0]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                for k in range(len(second.matrix[0])):
                    matrix_mult[i][j] += self.matrix[i][k] * second.matrix[k][j]
        matrix_result.set_matrix(matrix_mult)
        return matrix_result

    def __mul__(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        matrix_result = Matrix(len(self.matrix), len(self.matrix[0]))
        matrix_mult = [[0] * len(second.matrix[0]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                for k in range(len(second.matrix[0])):
                    matrix_mult[i][j] += self.matrix[i][k] * second.matrix[k][j]
        matrix_result.set_matrix(matrix_mult)
        return matrix_result

    def write_to_file(self, name_of_file):
        res = ""
        f = open(name_of_file, 'w')
        for row in self.matrix:
            for element in row:
                res += str(element) + " "
            res += '\n'
        f.write(res)
        f.close()

    def __str__(self):
        res = ""
        for row in self.matrix:
            for element in row:
                res += str(element) + " "
            res += '\n'
        return res
