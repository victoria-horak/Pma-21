from lengthNotMatchExeption import LengthNotMatchExeption
from DetException import DetException


class Matrix:
    def __init__(self, matrix):
        self.__matrix = Matrix.filling(self, matrix)

    def trans(self, matrix):
        matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
        return matrix

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
            if determinant == 0:
                raise DetException('matrix determinant==0')
        elif len(self.__matrix) == 2 and len(self.__matrix[0]) == 2:
            determinant = self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[1][0] * self.__matrix[0][1]
        elif len(self.__matrix) == 1 and len(self.__matrix[0]) == 1:
            determinant += self.__matrix[0][0]
        return determinant

    def minor(self, rows, column):
        matrix = []
        for i in range(len(self.__matrix)):
            row = []
            for j in range(len(self.__matrix[0])):
                if i != rows and j != column:
                    row.append(self.__matrix[i][j])
            matrix.append(row)
        matrix = [x for x in matrix if x]
        return matrix

    def inverse(self):
        matrix = []
        counter = 1
        for i in range(len(self.__matrix)):
            row = []
            for j in range(len(self.__matrix[0])):
                element = Matrix.det(Matrix(Matrix.minor(self, i, j)))
                if len(self.__matrix) == 3:
                    if counter % 2 == 0:
                        element = element * (-1)
                elif len(self.__matrix) == 2:
                    if counter == 2 or counter == 3:
                        element = element * (-1)
                counter += 1
                row.append(element)
            matrix.append(row)
        determinant = self.det()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix[i][j] / determinant
        return matrix

    def __truediv__(self, other):
        if len(self.__matrix[0]) == len(other.__matrix):
            result = []
            matrixInverse = Matrix.trans(self, Matrix.inverse(other))
            for i in range(len(self.__matrix)):
                row = []
                for j in range(len(matrixInverse[0])):
                    temp = float()
                    for x in range(len(matrixInverse)):
                        temp += self.__matrix[i][x] * matrixInverse[x][j]
                    row.append(round(temp,3))
                result.append(row)
            return Matrix(result)
        else:
            raise LengthNotMatchExeption('Size matrix is bad')

    def __mul__(self, other):
        if len(self.__matrix[0]) != len(other.__matrix):
            raise LengthNotMatchExeption("Matrix don't mult")
        else:
            matrixResult = []
            for i in range(len(self.__matrix)):
                row = []
                for j in range(len(other.__matrix[0])):
                    suma = int()
                    for x in range(len(self.__matrix[0])):
                        suma += self.__matrix[i][x] * other.__matrix[x][j]
                    row.append(suma)
                matrixResult.append(row)
            return Matrix(matrixResult)

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
        matrixResult = []
        if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[0]) != len(other.__matrix[0]):
            raise LengthNotMatchExeption("Matrix length not match")
        for i in range(len(self.__matrix)):
            row = []
            for j in range(len(self.__matrix[0])):
                temp = self.__matrix[i][j] + other.__matrix[i][j]
                row.append(temp)
            matrixResult.append(row)
        return Matrix(matrixResult)

    def __sub__(self, other):
        matrixResult = []
        if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[0]) != len(other.__matrix[0]):
            raise LengthNotMatchExeption("Matrix length not match")
        for i in range(len(self.__matrix)):
            row = []
            for j in range(len(self.__matrix[0])):
                temp = self.__matrix[i][j] - other.__matrix[i][j]
                row.append(temp)
            matrixResult.append(row)
        return Matrix(matrixResult)

    def __str__(self):
        result = ""
        for row in self.__matrix:
            for item in row:
                result += str(item) + " "
            result += "\n"
        return result

    def writeToFile(self, nameFile):
        with open(nameFile, "a") as file:
            file.write(str(self))

    @classmethod
    def sum_matrix(cls, matrixFirst, matrixSecond):
        return cls(matrixFirst + matrixSecond)

    @classmethod
    def sub_matrix(cls, matrixFirst, matrixSecond):
        return cls(matrixFirst - matrixSecond)

    def __len__(self):
        return len(self.__matrix)

    def __getitem__(self, key):
        return self.__matrix[key]
