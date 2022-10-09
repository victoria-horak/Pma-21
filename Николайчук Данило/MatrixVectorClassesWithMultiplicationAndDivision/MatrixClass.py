from differentExceptions import *


class Matrix:
    pass


class Matrix:
    def __init__(self, matrix=[]):
        self.matrix = []
        if type(matrix) == int or type(matrix) == float or type(matrix) == chr or type(matrix) == str:
            raise DifferentError('not matrix')
        elif matrix != []:
            self.matrix = matrix

    def fillConsole(self):
        lengthRows = 0
        lengthColumns = 0
        try:
            lengthRows = int(input("Enter length of rows: "))
            lengthColumns = int(input("Enter length of columns: "))
        except ValueError as exc:
            print("Error" + str(exc))
            exit()
        for rowIterator in range(0, lengthRows):
            row = []
            for columnIterator in range(0, lengthColumns):
                element = 0
                try:
                    element = int(input(f"Enter element matrix[{rowIterator}][{columnIterator}]: "))
                except ValueError as exc:
                    print("Error" + str(exc))
                    exit()
                row.append(element)
            self.matrix.append(row)

    @classmethod
    def fillConsoleStatic(cls):
        matrix = Matrix()
        matrix.fillConsole()
        return matrix

    @classmethod
    def fillFromFileStatic(cls, fileName):
        matrix = Matrix()
        matrix.fillFromFile(fileName)
        return matrix

    def fillFromFile(self, fileName):
        file = open(fileName)
        lines = file.readlines()
        for rowIterator in range(0, len(lines)):
            if lines[rowIterator].isspace():
                continue
            row = []
            lineOfSplit = lines[rowIterator].split(",")
            if len(self.matrix) >= 1 and len(self.matrix[len(self.matrix) - 1]) != len(lineOfSplit):
                raise DifferentError('size of columns is not same.')
            for columnIterator in range(0, len(lineOfSplit)):
                try:
                    element = int(lineOfSplit[columnIterator])
                    row.append(element)
                except ValueError as exc:
                    print(exc)
                    exit(0)
            self.matrix.append(row)
        file.close()

    def add(self, other):
        if (len(self.matrix) != len(other.matrix)):
            raise DifferentError('we can\'t add this two matrix(not same number of rows).')
        if (len(self.matrix[0]) != len(other.matrix[0])):
            raise DifferentError('we can\'t add this two matrix(not same number of columns).')
        matrix = []
        for rowIterator in range(0, len(self.matrix)):
            row = []
            for columIterator in range(0, len(self.matrix[rowIterator])):
                row.append(self.matrix[rowIterator][columIterator] + other.matrix[rowIterator][columIterator])
            matrix.append(row)
        return Matrix(matrix)

    @classmethod
    def addStatic(cls, matrix1, matrix2):
        return matrix1.add(matrix2)

    def __add__(self, other):
        return self.add(other)

    def sub(self, other):
        if (len(self.matrix) != len(other.matrix)):
            raise DifferentError('we can\'t subtract this two matrix(not same number of rows).')
        if (len(self.matrix[0]) != len(other.matrix[0])):
            raise DifferentError('we can\'t subtract this two matrix(not same number of columns).')
        matrix = []
        for rowIterator in range(0, len(self.matrix)):
            row = []
            for columIterator in range(0, len(self.matrix[rowIterator])):
                row.append(self.matrix[rowIterator][columIterator] - other.matrix[rowIterator][columIterator])
            matrix.append(row)
        return Matrix(matrix)

    def __sub__(self, other):
        return self.sub(other)

    @classmethod
    def subStatic(cls, matrix1, matrix2):
        return matrix1.sub(matrix2)

    def fillingMatrixWithZeros(self, lenthOfRows, lenthOfColumns):
        for rowIterator in range(0, lenthOfRows):
            row = []
            for columnIterator in range(0, lenthOfColumns):
                row.append(0)
            self.matrix.append(row)

    def multiplication(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise DifferentError('matrix of this sizes can`t be multiplicate.')
        resultMatrix = Matrix()
        resultMatrix.fillingMatrixWithZeros(len(self.matrix), len(other.matrix[0]))
        for rowIterator in range(0, len(self.matrix)):
            for columnIterator in range(0, len(other.matrix[0])):
                for inColumnIterator in range(0, len(other.matrix)):
                    resultMatrix.matrix[rowIterator][columnIterator] += self.matrix[rowIterator][inColumnIterator] * \
                                                                        other.matrix[inColumnIterator][columnIterator]
        return resultMatrix

    def __mul__(self, other):
        return self.multiplication(other)

    @classmethod
    def multiplicationStatic(cls, matrix1, matrix2):
        return matrix1.multiplication(matrix2)

    def trans(self):
        resultMatrix = Matrix()
        for rowIterator in range(0, len(self.matrix[0])):
            row = []
            for columnsIterator in range(len(self.matrix)):
                row.append(self.matrix[columnsIterator][rowIterator])
            resultMatrix.matrix.append(row)
        return resultMatrix

    def getMatr(self, matrix: Matrix(), columnSize, rowSize=0):
        rowTempIterator = 0
        for rowIterator in range(0, len(matrix.matrix)):
            if rowIterator != rowSize:
                columnTempIt = 0
                for columnIterator in range(len(matrix.matrix)):
                    if columnIterator != columnSize:
                        self.matrix[rowTempIterator][columnTempIt] = matrix.matrix[rowIterator][columnIterator]
                        columnTempIt += 1
                rowTempIterator += 1

    def determinator(self):
        tempNumbverOfDet = 0
        pow = 1
        if len(self.matrix) < 1:
            raise DifferentError("we can`t find the determinant for a matrix of this size")
        elif len(self.matrix) == 1:
            tempNumbverOfDet = self.matrix[0][0]
        elif len(self.matrix) == 2:
            tempNumbverOfDet = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
        else:
            for rowIterator in range(len(self.matrix)):
                tempMatrix = Matrix()
                tempMatrix.fillingMatrixWithZeros(len(self.matrix) - 1, len(self.matrix) - 1)
                tempMatrix.getMatr(self, rowIterator)
                tempNumbverOfDet = tempNumbverOfDet + pow * self.matrix[0][rowIterator] * tempMatrix.determinator()
                pow = -pow
        return tempNumbverOfDet

    def divisionOfMatrix(self, other):
        if len(self.matrix) != len(other.matrix):
            raise DifferentError("different size can`t divide them.")
        determinator = other.determinator()
        if determinator == 0:
            raise DifferentError("Determinator of matrix == 0, program can`t devite such matrix.")
        matrixAfterAllOperations = Matrix()
        matrixAfterAllOperations.fillingMatrixWithZeros(len(other.matrix), len(other.matrix))
        for rowIterator in range(len(other.matrix)):
            for columnIterator in range(len(other.matrix)):
                tempMatrix = Matrix()
                tempMatrix.fillingMatrixWithZeros(len(other.matrix) - 1, len(other.matrix) - 1)
                tempMatrix.getMatr(other, columnIterator, rowIterator)
                matrixAfterAllOperations.matrix[rowIterator][columnIterator] = pow(-1.0,
                                                                                   rowIterator + columnIterator + 2) * tempMatrix.determinator() / determinator
        matrixAfterAllOperations = matrixAfterAllOperations.trans()
        return self * matrixAfterAllOperations

    def __truediv__(self, other):
        return self.divisionOfMatrix(other)

    @classmethod
    def divisionStatic(cls, matrix1, matrix2):
        return matrix1.divisionOfMatrix(matrix2)

    @classmethod
    def showStatic(cls, matrix):
        matrix.show()

    def show(self):
        if len(self.matrix) == 0:
            raise DifferentError('matrix size is zero.')
        for rowIterator in range(0, len(self.matrix)):
            print(self.matrix[rowIterator])

    @classmethod
    def fillFileWithMatrixStatic(cls, matrix, file):
        matrix.fillFileWithMatrix(file)

    def fillFileWithMatrix(self, file):
        if len(self.matrix) == 0:
            raise DifferentError('matrix size is zero.')
        for rowIterator in range(0, len(self.matrix)):
            for columnIterator in range(0, len(self.matrix)):
                if len(self.matrix[rowIterator]) - 1 == columnIterator:
                    file.write(str(self.matrix[rowIterator][columnIterator]))
                    file.write("\n")
                else:
                    file.write(str(self.matrix[rowIterator][columnIterator]))
                    file.write(",")
