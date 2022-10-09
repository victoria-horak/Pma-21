from differSize import *
from InvalidDimensionsForMatrixMultiplication import *


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def read_matrix(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                temporary = [elem for elem in line.strip().split(",")]
                temporary = [int(element) for element in temporary if element]
                self.matrix.append(temporary)
            self.matrix = [elem for elem in self.matrix if elem]
        file.close()
        return self.matrix

    def __str__(self):
        str_matrix = ''
        for iterator in self.matrix:
            str_matrix += str(iterator) + '\n'
        return str_matrix

    def __len__(self):
        return len(self.matrix)

    def get_matrix(self):
        return self.matrix

    def write(self, file_name):
        file = open(file_name, 'a')
        for iterator in self.matrix:
            file.write(str(iterator) + '\n')
        file.write('\n')
        file.close()

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            first = [[self.matrix[iterator][jterator] + other.matrix[iterator][jterator] for jterator in
                      range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(first)
        else:
            raise differSize("\nMatrices don`t have the same size!")

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            first = [[self.matrix[iterator][jterator] - other.matrix[iterator][jterator] for jterator in
                      range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(first)
        else:
            raise differSize("\nMatrices don`t have the same size!")

    def __mul__(self, other):
        if len(self.matrix) == len(other.matrix[0]) and len(self.matrix[0]) == len(other.matrix):
            result = []
            for row_of_matrix in range(len(self.matrix)):
                result.append([0 for column_of_matrix in range(len(other.matrix[0]))])
            # print("RESULT BEFORE:\n", result)
            for iterator in range(len(self.matrix)):
                for jterator in range(len(other.matrix[iterator])):
                    for kterator in range(len(other.matrix)):
                        result[iterator][jterator] += self.matrix[iterator][kterator] * other.matrix[kterator][jterator]
            return Matrix(result)
        else:
            raise InvalidDimensionsForMatrixMultiplication("\nMatrices don`t have the valid size for multiplication!")

    def __truediv__(self, other):
        try:
            if len(self.matrix) == len(other.matrix[0]) and len(self.matrix[0]) == len(other.matrix):
                result = []
                for row_of_matrix in range(len(self.matrix)):
                    result.append([0 for column_of_matrix in range(len(other.matrix[0]))])
                # print("RESULT BEFORE:\n", result)
                for iterator in range(len(self.matrix)):
                    for jterator in range(len(other.matrix[iterator])):
                        for kterator in range(len(other.matrix)):
                            result[iterator][jterator] += self.matrix[iterator][kterator] / other.matrix[kterator][
                                jterator]
                return Matrix(result)
            else:
                raise InvalidDimensionsForMatrixMultiplication("\nMatrices don`t have the valid size for "
                                                               "multiplication!")
        except ZeroDivisionError:
            with open('result_matrix.txt', "a+") as file_matrix:
                file_matrix.write("We cannot divide by zero!")
            return Matrix([])

    @classmethod
    def add_static(cls, first_matrix: "Matrix", second_matrix: "Matrix") -> "Matrix":
        return first_matrix + second_matrix

    @classmethod
    def sub_static(cls, first_matrix: "Matrix", second_matrix: "Matrix") -> "Matrix":
        return first_matrix - second_matrix

    @classmethod
    def mul_static(cls, first_matrix: "Matrix", second_matrix: "Matrix") -> "Matrix":
        return first_matrix * second_matrix

    @classmethod
    def div_static(cls, first_matrix: "Matrix", second_matrix: "Matrix") -> "Matrix":
        return first_matrix * second_matrix

    # @property
    # def transpose_matrix(self):
    #     matrix1 = self.matrix
    #     for iterator in range(len(matrix[0])):
    #         matrix2 = self.matrix
    #         for jterator in matrix:
    #             matrix2.append(jterator[iterator])
    #         matrix1.append(matrix2)
    #     return matrix1
