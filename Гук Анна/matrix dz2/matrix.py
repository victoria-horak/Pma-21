from error_size1 import Error_size


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def read_matrix_from_file(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                read_matrix = [element for element in line.replace(" ", "").replace("\n", "")]
                read_matrix = [int(element) for element in read_matrix]
                self.matrix.append(read_matrix)
            self.matrix = [element for element in self.matrix if element]
        file.close()
        return self.matrix



    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            result_mat = [[self.matrix[iterator][jterator] + other.matrix[iterator][jterator] for jterator in
                        range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(result_mat)
        else:
            raise Error_size("Error!!! Matrices have different sizes!!!\n")

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            result_mat = [[self.matrix[iterator][jterator] - other.matrix[iterator][jterator] for jterator in
                        range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(result_mat)
        else:
            raise Error_size("Error!!! Matrices have different sizes!!!\n")

    def __str__(self):
        line = ''
        for row in self.matrix:
            for element in row:
                line += str(element) + ' '
            line += "\n"
        return line