from Exceptions.InvalidLengthException import InvalidLenghtException
from Exceptions.DeterminantException import DeterminantException
import numpy as num


def matrix_transport(matrix):
    matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    return matrix


class Matrix:
    def __init__(self, matrix):
        if type(matrix) is list:
            self.__matrix = matrix
        if type(matrix) is str:
            self.__matrix = Matrix.read_matrix_from_file(self, matrix)

    def __mul__(self, other):
        if len(self.__matrix[0]) == len(other.__matrix):
            result = []
            for i in range(len(self.__matrix)):
                row = []
                for j in range(len(other.__matrix[0])):
                    row.append(0)
                result.append(row)
            for row in range(len(self.__matrix)):
                for column in range(len(other.__matrix[0])):
                    for iterator in range(len(other.__matrix)):
                        result[row][column] += self.__matrix[row][iterator] * other.__matrix[iterator][column]
            return Matrix(result)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    def det(self):
        determinant = 0
        if len(self.__matrix) == 3 and len(self.__matrix[0]) == 3:
            determinant = self.__matrix[0][0] * self.__matrix[1][1] * self.__matrix[2][2] + self.__matrix[0][1] * \
                          self.__matrix[1][2] * \
                          self.__matrix[2][0] + self.__matrix[0][2] * self.__matrix[1][0] * self.__matrix[2][1] - \
                          self.__matrix[0][2] * \
                          self.__matrix[1][1] * self.__matrix[2][0] - self.__matrix[0][1] * self.__matrix[1][0] * \
                          self.__matrix[2][2] - \
                          self.__matrix[0][0] * self.__matrix[1][2] * self.__matrix[2][1]
            if determinant != 0:
                return determinant
            else:
                raise DeterminantException('matrix determinant==0')

        elif len(self.__matrix) == 2 and len(self.__matrix[0]) == 2:
            determinant = self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[1][0] * self.__matrix[0][1]
            if determinant != 0:
                return determinant
            else:
                raise DeterminantException('matrix determinant==0')
        elif len(self.__matrix) == 1 and len(self.__matrix[0]) == 1:
            determinant += self.__matrix[0][0]
            if determinant != 0:
                return determinant
            else:
                raise DeterminantException('matrix determinant==0')

    def minor(self, rows, column):
        matrix = []
        for iterator in range(len(self.__matrix)):
            row = []
            for jterator in range(len(self.__matrix[0])):
                if iterator != rows and jterator != column:
                    row.append(self.__matrix[iterator][jterator])
            matrix.append(row)
        matrix = [x for x in matrix if x]
        return matrix

    def reverse(self):
        matrix2 = []
        numeric = 1
        for iterator in range(len(self.__matrix)):
            row = []
            for jterator in range(len(self.__matrix[0])):
                element = Matrix.det(Matrix(Matrix.minor(self, iterator, jterator)))
                if len(self.__matrix) == 3:
                    if numeric % 2 == 0:
                        element = element * (-1)
                elif len(self.__matrix) == 2:
                    if numeric == 2 or numeric == 3:
                        element = element * (-1)
                numeric += 1
                row.append(element)
            matrix2.append(row)
        return matrix2

    def __truediv__(self, other):
        if len(self.__matrix[0]) == len(other.__matrix):
            result = [[0 for x in range(len(other.__matrix[0]))] for y in range(len(self.__matrix))]
            determinant = Matrix.det(other)
            matrix_obernena = Matrix.reverse(other)
            matrix_obernena = matrix_transport(matrix_obernena)
            matrix_obernena = [[round(matrix_obernena[iterator][jterator] / determinant, 2) for jterator in
                                range(len(matrix_obernena[0]))] for
                               iterator in range(len(matrix_obernena))]
            for i in range(len(self.__matrix)):
                for j in range(len(matrix_obernena[0])):
                    for k in range(len(matrix_obernena)):
                        result[i][j] += self.__matrix[i][k] * matrix_obernena[k][j]
                        result[i][j] = round(result[i][j], 2)
            return Matrix(result)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    def read_matrix_from_file(self, file_name):
        with open(file_name, "r") as file:
            matrix = []
            for line in file:
                list = [element for element in line.strip().split(",")]
                list = [int(element) for element in list if element]
                matrix.append(list)
            matrix = [x for x in matrix if x]
        file.close()
        return matrix

    def __len__(self):
        return len(self.__matrix)

    def __getitem__(self, index):
        return self.__matrix[index]

    @classmethod
    def add_matrix_static(cls, matrix1, matrix2):
        return cls(matrix1 + matrix2)

    def __add__(self, other):
        if len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0]):
            matrix1 = [[self.__matrix[iterator][jterator] + other.__matrix[iterator][jterator] for jterator in
                        range(len(self.__matrix[0]))] for iterator in range(len(self.__matrix))]
            return Matrix(matrix1)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    @classmethod
    def sub_matrix_static(cls, matrix1, matrix2):
        return cls(matrix1 - matrix2)

    def __sub__(self, other):
        if len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0]):
            matrix1 = [[self.__matrix[iterator][jterator] - other.__matrix[iterator][jterator] for jterator in
                        range(len(self.__matrix[0]))] for iterator in range(len(self.__matrix))]
            return Matrix(matrix1)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    @classmethod
    def add_matrix(cls, matrix1, matrix2):
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            matrix1 = [[matrix1[iterator][jterator] + matrix2[iterator][jterator] for jterator in
                        range(len(matrix1[0]))] for iterator in range(len(matrix1))]
            return cls(matrix1)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    def __str__(self):
        string = ''
        for iterator in self.__matrix:
            string += str(iterator) + '\n'
        return string

    def write_to_file(self, file_name):
        with open(file_name, 'a') as file:
            for iterator in self.__matrix:
                file.write(str(iterator) + '\n')
            file.write('\n')
        file.close()

    @classmethod
    def write_to_file_static(cls, file_name, matrix):
        with open(file_name, 'a') as file:
            for iterator in matrix:
                file.write(str(iterator) + '\n')
            file.write('\n')
        file.close()
