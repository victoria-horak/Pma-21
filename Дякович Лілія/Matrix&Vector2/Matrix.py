from LengthError import LengthErrorException
from ErrorDivision import ErrorDivision


class Matrix:

    def __init__(self, matrix):
        self.__matrix = Matrix.filling(self, matrix)

    def filling(self, matrix):
        if type(matrix) is str:
            return Matrix.readFromFile(self, matrix)
        else:
            return matrix

    def readFromFile(self, nameFile=""):
        with open(nameFile, "r") as file:
            matrix = []
            for line in file.readlines():
                row = [item for item in line.strip().split(",")]
                row = [int(item) for item in row if item]
                matrix.append(row)
            matrix = [item for item in matrix if item]
        return matrix

    def __add__(self, other):
        if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[0]) != len(other.__matrix[0]):
            raise LengthErrorException("matrices have different sizes")
        else:
            result = Matrix([])
            result.__matrix = []
            for i in range(len(self.__matrix)):
                col = []
                for j in range(len(self.__matrix[i])):
                    col.append(self.__matrix[i][j] + other.__matrix[i][j])
                result.__matrix.append(col)
            return result

    def __mul__(self, other):
        if len(self.__matrix[0]) != len(other.__matrix):
            raise LengthErrorException(
                "the number of elements in the row of the first matrix is not equal to the number of elements in the column of the second\n")
        else:
            result = [[0 for col in range(len(other.__matrix[0]))] for row in range(len(self.__matrix))]
            for i in range(len(self.__matrix)):
                for j in range(len(other.__matrix[0])):
                    for k in range(len(other.__matrix)):
                        result[i][j] += self.__matrix[i][k] * other.__matrix[k][j]
            return Matrix(result)

    @classmethod
    def add_matrix(cls, matrix1=None, matrix2=None):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise LengthErrorException("matrices have different sizes\n")
        else:
            result = []
            for i in range(len(matrix1)):
                col = []
                for j in range(len(matrix2[i])):
                    col.append(matrix1[i][j] + matrix2[i][j])
                result.append(col)
            return cls(result)

    def __sub__(self, other):
        if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[0]) != len(other.__matrix[0]):
            raise LengthErrorException("matrices have different sizes\n")
        else:
            result = Matrix()
            result.__matrix = []
            for i in range(len(self.__matrix)):
                col = []
                for j in range(len(self.__matrix[i])):
                    col.append(self.__matrix[i][j] - other.__matrix[i][j])
                result.__matrix.append(col)
            return result

    @classmethod
    def sub_matrix(cls, matrix1=None, matrix2=None):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise LengthErrorException("matrices have different sizes")
        else:
            result = []
            for i in range(len(matrix1)):
                col = []
                for j in range(len(matrix2[i])):
                    col.append(matrix1[i][j] - matrix2[i][j])
                result.append(col)
            return cls(result)

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

    @classmethod
    def matrixMultStut(cls, matrix1, matrix2):
        if len(matrix1[0]) != len(matrix2):
            raise LengthErrorException(
                "the number of elements in the row of the first matrix is not equal to the number of elements in the column of the second\n")
        else:
            result = [[0 for col in range(len(matrix2[0]))] for row in range(len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        result[i][j] += matrix1[i][k] * matrix2[k][j]
            return cls(result)

    def det(self):
        determinant = 0
        if len(self.__matrix) == 3:
            determinant = self.__matrix[0][0] * self.__matrix[1][1] * self.__matrix[2][2] + self.__matrix[0][1] * \
                          self.__matrix[1][2] * \
                          self.__matrix[2][0] + self.__matrix[0][2] * self.__matrix[1][0] * self.__matrix[2][1] - \
                          self.__matrix[0][2] * \
                          self.__matrix[1][1] * self.__matrix[2][0] - self.__matrix[0][1] * self.__matrix[1][0] * \
                          self.__matrix[2][2] - \
                          self.__matrix[0][0] * self.__matrix[1][2] * self.__matrix[2][1]
            return determinant
        elif len(self.__matrix) == 2:
            determinant = self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[1][0] * self.__matrix[0][1]
            return determinant
        elif len(self.__matrix) == 1:
            determinant += self.__matrix[0][0]
            return determinant

    def obernena(self):
        result = [[0 for col in range(len(self.__matrix[0]))] for row in range(len(self.__matrix))]
        determinant = self.det()
        # тут зробити ерорку детермінанту
        if determinant == 0:
            raise ErrorDivision("determinant of the matrix = 0 \n")
        else:
            if len(self.__matrix) == 3 and len(self.__matrix[0]) == 3:
                first = self.__matrix[1][1] * self.__matrix[2][2] - self.__matrix[1][2] * self.__matrix[2][1]
                second = -(self.__matrix[0][1] * self.__matrix[2][2] - self.__matrix[2][1] * self.__matrix[0][2])
                third = self.__matrix[0][1] * self.__matrix[1][2] - self.__matrix[1][1] * self.__matrix[0][2]
                fourth = -(self.__matrix[1][0] * self.__matrix[2][2] - self.__matrix[2][0] * self.__matrix[1][2])
                fifth = self.__matrix[0][0] * self.__matrix[2][2] - self.__matrix[0][2] * self.__matrix[2][0]
                sixth = -(self.__matrix[0][0] * self.__matrix[1][2] - self.__matrix[1][0] * self.__matrix[0][2])
                seventh = self.__matrix[1][0] * self.__matrix[2][1] - self.__matrix[2][0] * self.__matrix[1][1]
                eigthth = -(self.__matrix[0][0] * self.__matrix[2][1] - self.__matrix[2][0] * self.__matrix[0][1])
                nineth = self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[1][0] * self.__matrix[0][1]
                obernenaMatrix = [[first, second, third], [fourth, fifth, sixth], [seventh, eigthth, nineth]]
                for i in range(len(obernenaMatrix)):
                    for j in range(len(obernenaMatrix[0])):
                        result[i][j] += round(obernenaMatrix[i][j] / determinant, 2)
            elif len(self.__matrix) == 2 and len(self.__matrix[0]) == 2:
                first = self.__matrix[1][1]
                second = -(self.__matrix[0][1])
                third = -(self.__matrix[1][0])
                fourth = self.__matrix[0][0]
                obernenaMatrix = [[first, second], [third, fourth]]
                for i in range(len(obernenaMatrix)):
                    for j in range(len(obernenaMatrix[0])):
                        result[i][j] += round(obernenaMatrix[i][j] / determinant, 2)
            elif len(self.__matrix) == 1 and len(self.__matrix[0]) == 1:
                first = self.__matrix[0][0]
                result[0][0] = first
            return Matrix(result)

    def __getitem__(self, x):
        return self.__matrix[x]

    def __truediv__(self, other):
        if len(self.__matrix) > 3 or len(self.__matrix[0]) > 3:
            raise ErrorDivision("do not calculate the matrix of this size \n")
        else:
            result = [[0 for col in range(len(other.__matrix[0]))] for row in range(len(self.__matrix))]
            obernenaMatrix = Matrix.obernena(other)
            for i in range(len(self.__matrix)):
                for j in range(len(obernenaMatrix[0])):
                    for k in range(len(other.__matrix)):
                        result[i][j] += round(self.__matrix[i][k] * obernenaMatrix[k][j])
            return Matrix(result)

    @classmethod
    def truedivStatic(cls, matrix1, matrix2):
        if len(matrix1) > 3 or len(matrix2[0]) > 3:
            raise ErrorDivision("do not calculate the matrix of this size \n")
        else:
            result = [[0 for col in range(len(matrix2[0]))] for row in range(len(matrix1))]
            obernenaMatrix = Matrix.obernena(Matrix(matrix2))
            for i in range(len(matrix1)):
                for j in range(len(obernenaMatrix[0])):
                    for k in range(len(matrix2)):
                        result[i][j] += matrix1[i][k] * obernenaMatrix[k][j]
                        result[i][j] = round(result[i][j], 2)
            return cls(result)
