class WrongSize(Exception):
    """The size of two matrices is not the same"""


class Matrix:
    def __init__(self, data):
        self.matrix = data

    @staticmethod
    def read_from_file(file_name):
        with open(file_name, 'r') as file:
            matrix = []
            for row in file:
                if row.strip() == "":
                    continue
                matrix.append([int(element) for element in row.split(',')])
        return matrix

    def get_matrix(self):
        return self.matrix

    def add(self, other):
        if len(self.matrix) != len(other.get_matrix()) or len(self.matrix[0]) != len(other.get_matrix()[0]):
            raise WrongSize("The matrices have different size!!!")
        result = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = (self.matrix[i][j] + other.get_matrix()[i][j])
        return result

    def subtract(self, other):
        if len(self.matrix) != len(other.get_matrix()) or len(self.matrix[0]) != len(other.get_matrix()[0]):
            raise WrongSize("The matrices have different size!!!")
        result = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = (self.matrix[i][j] - other.get_matrix()[i][j])
        return result

    def multiply(self, other):
        if len(self.matrix[0]) != len(other.get_matrix()):
            raise WrongSize("Number of columns in first matrix should be the same as number of rows in second")
        result = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(other.get_matrix()[0])):
                for k in range(len(other.get_matrix())):
                    result[i][j] += (self.matrix[i][k] * other.get_matrix()[k][j])
        return result

    def transpose(self):
        result = []
        for x in range(len(self.matrix[0])):
            result.append([0] * len(self.matrix))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[j][i] = self.matrix[i][j]
        return result

    @staticmethod
    def divide_matrices(m1, m2):
        return Matrix(m1.multiply(Matrix(m2.transpose())))

    def print(self):
        for row_iterator in range(len(self.matrix)):
            print(self.matrix[row_iterator])

    def write_to_file(self, name_of_file):
        f = open(name_of_file, 'w')
        for row_iterator in range(len(self.matrix)):
            f.write(str(self.matrix[row_iterator]) + '\n')
        f.close()
