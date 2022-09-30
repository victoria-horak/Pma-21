from DifferentSizes import *

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def read_matrix(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                temp_matrix = [element for element in line.strip().split(",")]
                temp_matrix = [int(element) for element in temp_matrix if element]
                self.matrix.append(temp_matrix)
            self.matrix = [element for element in self.matrix if element]
        file.close()
        return self.matrix


    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix1 = [[self.matrix[iterator][jterator] + other.matrix[iterator][jterator] for jterator in
                        range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(matrix1)
        else:
            file_name_result_exc = open('Dataresult.txt', 'a')
            file_name_result_exc.write("\nMatrixes have different sizes\n")
            file_name_result_exc.close()
            raise DifferentSizes("\nMatrixes have different sizes\n")

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix1 = [[self.matrix[iterator][jterator] - other.matrix[iterator][jterator] for jterator in
                        range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(matrix1)
        else:
            raise DifferentSizes("\nMatrixes have different sizes\n")

    def __str__(self):
        matrix_to_str = ''
        for iterator in self.matrix:
            matrix_to_str += str(iterator) + '\n'
        return matrix_to_str

    def write_to_file(self, file_name):
        file = open(file_name, 'a')
        for iterator in self.matrix:
            file.write(str(iterator) + '\n')
        file.write('\n')
        file.close()