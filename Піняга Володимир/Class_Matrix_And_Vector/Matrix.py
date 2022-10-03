from differSize import *

class Matrix():

    def __init__(self, matrix):
        self.matrix = matrix


    def read_matrix(self, fileName):
        with open(fileName, 'r') as file:
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


    def write(self, fileName):
        file = open(fileName, 'a')
        for iterator in self.matrix:
            file.write(str(iterator) + '\n')
        file.write('\n')
        file.close()


    def __add__(self, others):
        if len(self.matrix) == len(others.matrix) and len(self.matrix[0]) == len(others.matrix[0]):
            first = [[self.matrix[iterator][jterator] + others.matrix[iterator][jterator] for jterator in
                        range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(first)
        else:
            raise differSize("\nMatrixes don`t have the same size!")


    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            first = [[self.matrix[iterator][jterator] - other.matrix[iterator][jterator] for jterator in
                      range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(first)
        else:
            raise differSize("\nMatrixes don`t have the same size!")


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
