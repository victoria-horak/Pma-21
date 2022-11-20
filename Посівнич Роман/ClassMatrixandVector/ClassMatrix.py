from InvalidSize import *


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def enter_Matrix(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                temp_matrix = [element for element in line.strip().split(",")]
                temp_matrix = [int(element) for element in temp_matrix if element]
                self.matrix.addElements(temp_matrix)
            self.matrix = [element for element in self.matrix if element]
        file.close()
        return self.matrix

    def print_matrix_to_file(self, file_name):
        file = open(file_name, 'a')
        for iterator in self.matrix:
            file.write(str(iterator) + '\n')
        file.write('\n')
        file.close()

    def __str__(self):
        matrix_to_str = ''
        for iterator in self.matrix:
            matrix_to_str += str(iterator) + '\n'
        return matrix_to_str

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix = [[self.matrix[iterator][jterator] + other.matrix[iterator][jterator] for jterator in
                       range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(matrix)
        else:
            file = open('matrix3.txt', 'a')
            file.write("Matrices are of different sizes\n")
            raise InvalidSize("Matrices are of different sizes\n")

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix = [[self.matrix[iterator][jterator] - other.matrix[iterator][jterator] for jterator in
                       range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(matrix)
        else:
            raise InvalidSize("Matrices are of different sizes\n")

    def __mul__(self, other):
        if len(self.matrix) == len(other.matrix[0]):
            matrix = [[0 for column in range(len(other.matrix[0]))] for row in range(len(self.matrix))]
            for rows_of_first in range(len(self.matrix)):
                for columns_of_second in range(len(other.matrix[rows_of_first])):
                    for iterator in range(len(other.matrix)):
                        matrix[rows_of_first][columns_of_second] += \
                            self.matrix[rows_of_first][iterator] * other.matrix[iterator][columns_of_second]
            return Matrix(matrix)
        else:
            raise InvalidSize("Matrices are of different sizes\n")
