from IncorrectSize import IncorrectSize

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def readMatrix(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                temp_matrix = [element for element in line.replace(" ", "").replace("\n", "")]
                temp_matrix = [int(element) for element in temp_matrix]
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
            raise IncorrectSize("Error!!! Matrices have different sizes!!!\n")

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix1 = [[self.matrix[iterator][jterator] - other.matrix[iterator][jterator] for jterator in
                        range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(matrix1)
        else:
            raise IncorrectSize("Error!!! Matrices have different sizes!!!\n")

    def __str__(self):
        line = ''
        for row in self.matrix:
            for element in row:
                line += str(element) + ' '
            line += "\n"
        return line

