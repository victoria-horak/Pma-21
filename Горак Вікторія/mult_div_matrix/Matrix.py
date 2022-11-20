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
            number_count = 0
            for j in range(len(rows)):
                if (rows[j].isdigit()):
                    number_count += 1
            if (number_count != 0):
                matrix_first.append(" ".join(rows))
        file.close()

        self.matrix = [list(map(int, row.split())) for row in matrix_first]

    def mult_matrix(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise DifferentSize("The matrixes have different sizes")
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
            raise DifferentSize("The matrixes have different sizes")
        matrix_result = Matrix(len(self.matrix), len(self.matrix[0]))
        matrix_mult = [[0] * len(second.matrix[0]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                for k in range(len(second.matrix[0])):
                    matrix_mult[i][j] += self.matrix[i][k] * second.matrix[k][j]
        matrix_result.set_matrix(matrix_mult)
        return matrix_result

    def transposeMatrix(self):
        matrix_t = [[0] * len(self.matrix[0]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                matrix_t[i][j] = self.matrix[j][i]
        self.set_matrix(matrix_t)

    def getMatrixMinor(self, i, j):
        return [row[:j] + row[j + 1:] for row in (self.matrix[:i] + self.matrix[i + 1:])]

    def getMatrixDeternminant(self):
        if len(self.matrix) == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        determinant = 0
        for i in range(len(self.matrix)):
            minor = Matrix(1, 1)
            minor.set_matrix(self.getMatrixMinor(0, i))
            determinant += ((-1) ** i) * self.matrix[0][i] * minor.getMatrixDeternminant()
        return determinant

    def getMatrixInverse(self):
        determinant = self.getMatrixDeternminant()
        if determinant == 0:
            raise DifferentSize("determinant=0")
        if len(self.matrix) != len(self.matrix[0]):
            raise DifferentSize("The matrixes have different sizes")
        if len(self.matrix) == 2:
            if len(self.matrix) == 2:
                matrix_inv = Matrix(2, 2)
                matrix1 = [[0 for i in range(2)] for j in range(2)]
                matrix1[0][0] = self.matrix[1][1] / determinant
                matrix1[0][1] = self.matrix[0][1] / determinant
                matrix1[1][0] = self.matrix[1][0] / determinant
                matrix1[1][1] = self.matrix[1][1] / determinant
                matrix_inv.set_matrix(matrix1)
                return matrix_inv
        cofactors = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                minor = Matrix(len(self.matrix), len(self.matrix))
                minor.set_matrix(self.getMatrixMinor(i, j))
                cofactors[i][j] = (((-1) ** (i + j)) * (minor.getMatrixDeternminant()))
        matrix_result = Matrix(len(self.matrix), len(self.matrix[0]))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                cofactors[i][j] = cofactors[i][j] / determinant
            matrix_result.set_matrix(cofactors)
        matrix_result.transposeMatrix()
        return matrix_result

    def __truediv__(self, second):
        return self.mult_matrix(second.getMatrixInverse())

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
