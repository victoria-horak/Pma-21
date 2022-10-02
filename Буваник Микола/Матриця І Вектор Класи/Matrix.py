from lengthNotMatchExeption import LengthNotMatchExeption


class Matrix:
    def __init__(self, matrix=None):
        if matrix is None:
            self.__matrix = []
        else:
            self.__matrix = matrix

    @classmethod
    def readFromFile(cls, nameFile=""):
        with open(nameFile, "r") as file:
            matrix = []
            for line in file.readlines():
                row = [x for x in line.split(",")]
                row = [int(x) for x in row if x]
                matrix.append(row)
            _matrix = [x for x in matrix if x]
        return cls(matrix)

    def __add__(self, other):
        matrixResult = Matrix()
        if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[0]) != len(other.__matrix[0]):
            raise LengthNotMatchExeption("Matrix length not match")
        for i in range(len(self.__matrix)):
            row = []
            for j in range(len(self.__matrix[0])):
                temp = self.__matrix[i][j] + other.__matrix[i][j]
                row.append(temp)
            matrixResult.__matrix.append(row)
        return matrixResult

    def __sub__(self, other):
        matrixResult = Matrix()
        if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[0]) != len(other.__matrix[0]):
            raise LengthNotMatchExeption("Matrix length not match")
        for i in range(len(self.__matrix)):
            row = []
            for j in range(len(self.__matrix[0])):
                temp = self.__matrix[i][j] - other.__matrix[i][j]
                row.append(temp)
            matrixResult.__matrix.append(row)
        return matrixResult

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
        matrixResult = Matrix()
        if len(matrixFirst) != len(matrixSecond) or len(matrixFirst[0]) != len(matrixSecond[0]):
            raise LengthNotMatchExeption("Matrix length not match")
        for i in range(len(matrixFirst)):
            row = []
            for j in range(len(matrixFirst[0])):
                temp = matrixFirst[i][j] + matrixSecond[i][j]
                row.append(temp)
            matrixResult.__matrix.append(row)
        return matrixResult

    @classmethod
    def sub_matrix(cls, matrixFirst, matrixSecond):
        matrixResult = Matrix()
        if len(matrixFirst) != len(matrixSecond) or len(matrixFirst[0]) != len(matrixSecond[0]):
            raise LengthNotMatchExeption("Matrix length not match")
        for i in range(len(matrixFirst)):
            row = []
            for j in range(len(matrixFirst[0])):
                temp = matrixFirst[i][j] - matrixSecond[i][j]
                row.append(temp)
            matrixResult.__matrix.append(row)
        return matrixResult

    def __len__(self):
        return len(self.__matrix)

    def __getitem__(self, key):
        return self.__matrix[key]
