from differSize import *

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def read_Matrix(self, fileName):  # ввід з файлу
        with open(fileName, 'r') as file:
            matrix = [[element for element in matrix_str.strip().split(',')] for matrix_str in file]
        return matrix


    def write_to_file(self, matrix, fileName):  # запис у файл результату
        file = open(fileName, 'a')
        for iter in matrix:
            file.write(str(iter) + '\n')
        file.close()


    def __add__(self, others, fileName):
        if (len(self.matrix) != len(others.matrix) or len(self.matrix[0]) != len(others.matrix[0])):
            file = open(fileName, 'a')
            file.write(str(differSize("Matrixes don`t have same size!")) + '\n')

            raise differSize("Matrixes don`t have same size!")

        else:
            res_matrix = []
            for iter in range(len(matrix)):
                row = []
                for jter in range(len(self.matrix[0])):
                    row.append(0)
                res_matrix.append(row)
        for iter in range(len(self.matrix)):
            for jter in range(len(self.matrix)):
                res_matrix[iter][jter] = self.matrix[iter][jter] + others.matrix[iter][jter]
        return res_matrix


    def __sub__(self, others, fileName):
        if (len(self.matrix) != len(others.matrix) or len(self.matrix[0]) != len(others.matrix[0])):
            file = open(fileName, 'a')
            file.write(str(differSize("Matrixes don`t have same size!")) + '\n')

            raise differSize("Matrixes don`t have same size!")

        else:
            res_matrix = []
            for iter in range(len(matrix)):
                row = []
                for jter in range(len(self.matrix[0])):
                    row.append(0)
                res_matrix.append(row)
        for iter in range(len(self.matrix)):
            for jter in range(len(self.matrix)):
                res_matrix[iter][jter] = self.matrix[iter][jter] - others.matrix[iter][jter]
        return res_matrix
