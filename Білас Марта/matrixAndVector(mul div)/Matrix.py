from Exceptions import *


class Matrix:

    def __init__(self, matrix: int = []):
        try:
            self.matrix = matrix
        except ValueError:
            print("value error")
        pass

    def readFromFile(self, fileName):
        self.matrix = []
        with open(fileName) as file:
            try:
                for line in file:
                    if not line.isspace():
                        line = line.split(",")
                        row = []
                        for columnIterator in range(0, len(line)):
                            element = int(line[columnIterator])
                            row.append(element)
                        self.matrix.append(row)
            except ValueError:
                print("wrong element type")
                self.matrix.clear()

    @classmethod
    def staticReadFromFile(cls, fileName):
        result = Matrix()
        result.readFromFile(fileName)
        return result

    def printToFile(self, fileName):
        try:
            with open(fileName, "w") as file:
                if self.matrix == []:
                    raise Empty
                for i in range(0, len(self.matrix)):
                    file.write(str(self.matrix[i]) + " ")
                    file.write('\n')
        except Empty:
            print("vector is empty")

    @classmethod
    def staticPrintToFile(cls, matrix, fileName):
        matrix.printToFile(fileName)

    def __add__(self, other):
        result = Matrix()
        result.matrix = []
        try:
            if len(other.matrix) != len(self.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                raise DifferentLength()
            for rowIterator in range(0, len(self.matrix)):
                row = []
                for columnIterator in range(0, len(self.matrix[0])):
                    element = self.matrix[rowIterator][columnIterator] + other.matrix[rowIterator][columnIterator]
                    row.append(element)
                result.matrix.append(row)
        except DifferentLength:
            print("matrixes have different length")
        return result

    @classmethod
    def staticAdd(cls, firstMatrix, secondMatrix):
        result = Matrix()
        result = firstMatrix + secondMatrix
        return result

    def __sub__(self, other):
        result = Matrix()
        result.matrix = []
        try:
            if len(other.matrix) != len(self.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                raise DifferentLength()
            for rowIterator in range(0, len(self.matrix)):
                row = []
                for columnIterator in range(0, len(self.matrix[0])):
                    element = self.matrix[rowIterator][columnIterator] - other.matrix[rowIterator][columnIterator]
                    row.append(element)
                result.matrix.append(row)
        except DifferentLength:
            print("matrixes have different length")
        return result

    @classmethod
    def staticSub(cls, firstMatrix, secondMatrix):
        result = Matrix()
        result = firstMatrix - secondMatrix
        return result

    def transpose(self):
        result = Matrix()
        result.matrix = []
        for rowIterator in range(0, len(self.matrix[0])):
            row = []
            for columnIterator in range(0, len(self.matrix)):
                element = self.matrix[columnIterator][rowIterator]
                row.append(element)
            result.matrix.append(row)
        self.matrix = result.matrix

    def __mul__(self, other):
        result = Matrix()
        result.matrix = []
        element = 0
        try:
            if len(self.matrix) != len(other.matrix):
                raise DifferentLength()
            for i in range(0, len(self.matrix)):
                row = []
                for j in range(0, len(other.matrix[0])):
                    for k in range(0, len(self.matrix[0])):
                        element += self.matrix[i][k] * other.matrix[k][j]
                    row.append(element)
                    element = 0
                result.matrix.append(row)
        except DifferentLength:
            print("matrixes have different length")
        return result

    @classmethod
    def staticMul(cls, firstMatrix, secondMatrix):
        result = Matrix()
        result = firstMatrix * secondMatrix
        return result

    def determinant(self):
        result = 0
        if len(self.matrix) == 2:
            result = (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])
            return result
        if len(self.matrix) == 3:
            for i in range(0, 3):
                result += self.matrix[0][i] * (
                        self.matrix[1][(i + 1) % 3] * self.matrix[2][(i + 2) % 3] - self.matrix[1][(i + 2) % 3] *
                        self.matrix[2][(i + 1) % 3])
            return result

    def inverseMatrix(self):
        result = Matrix()
        result.matrix = []
        determinant = self.determinant()
        try:
            if len(self.matrix) != len(self.matrix[0]):
                raise DifferentLength()
            if len(self.matrix) > 3:
                raise FalseLength()
            if determinant == 0:
                raise ZeroDeterminat()
            if len(self.matrix) == 2:
                result.matrix = [([0] * 2) for i in range(2)]
                result.matrix[0][0]=self.matrix[1][1]/determinant
                result.matrix[0][1] = (-1)*self.matrix[0][1] / determinant
                result.matrix[1][0] = (-1)*self.matrix[1][0] / determinant
                result.matrix[1][1] = self.matrix[0][0] / determinant
                self.matrix = result.matrix
            if len(self.matrix) == 3:
                for i in range(0, 3):
                    row = []
                    for j in range(0, 3):
                        element = ((self.matrix[(j + 1) % 3][(i + 1) % 3] * self.matrix[(j + 2) % 3][(i + 2) % 3]) - (
                                self.matrix[(j + 1) % 3][(i + 2) % 3] * self.matrix[(j + 2) % 3][
                            (i + 1) % 3])) / determinant
                        row.append(element)
                    result.matrix.append(row)
                self.matrix = result.matrix
        except DifferentLength:
            print("matrix is not squared")
        except FalseLength:
            print("size of matrix is >3")
        except ZeroDeterminat:
            print("determinat can not be zero")

    def __truediv__(self, other):
        result = Matrix()
        result.matrix = []
        element = 0
        try:
            if len(self.matrix) != len(other.matrix):
                raise DifferentLength()
            other.inverseMatrix()
            result = self * other
            return result
        except DifferentLength:
            print("matrixes have different length")

    @classmethod
    def staticDiv(cls, firstMatrix, secondMatrix):
        result = Matrix()
        result = firstMatrix / secondMatrix
        return result
