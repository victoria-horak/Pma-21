import sys
from ExceptionsMatrix import *

class Matrix:
    pass

class Matrix:
    def __init__(self, matrix = None):
        self.matrix = []
        if type(matrix) == int or type(matrix) == float or type(matrix) == chr or type(matrix)== str:
            raise NotMatrix('not matrix')
        elif matrix != None:
            self.matrix = matrix

    def __len__(self):
        return len(self.matrix)

    def lenOfColumn(self, rowIterator):
        return len(self.matrix[rowIterator])

    def elementRow(self, rowIterator):
        return self.matrix[rowIterator]

    def elementRowCol(self, rowIterator, columnIterator):
        return self.matrix[rowIterator][columnIterator]

    @classmethod
    def fillConsole(cls):
        try:
            lengthRows = int(input("Enter length of rows: "))
            lengthColumns = int(input("Enter length of columns: "))
        except ValueError as exc:
            print("Error" + str(exc))
            sys.exit(1)
        matrix = []
        for rowIterator in range(0, lengthRows):
            row = []
            for columnIterator in range(0, lengthColumns):
                try:
                    element = int(input(f"Enter element matrix[{rowIterator}][{columnIterator}]: "))
                except ValueError as exc:
                    print("Error" + str(exc))
                    sys.exit(1)
                row.append(element)
            matrix.append(row)
        return cls(matrix)

    @classmethod
    def fillFromFileStatic(cls, fileName):
        matrix = []
        file = open(fileName)
        lines = file.readlines()
        for rowIterator in range(0, len(lines)):
            row = []
            lineOfSplit = lines[rowIterator].split(",")
            for columnIterator in range(0, len(lineOfSplit)):
                if lineOfSplit[0] == "\n":
                    break
                try:
                    element = int(lineOfSplit[columnIterator])
                    row.append(element)
                except ValueError as exc:
                    print(exc)
                    sys.exit(1)
            if len(row) != 0:
                matrix.append(row)
        file.close()
        return cls(matrix)

    def fillFromFile(self, fileName):
        file = open(fileName)
        lines = file.readlines()
        for rowIterator in range(0,len(lines)):
            row = []
            lineOfSplit = lines[rowIterator].split(",")
            for columnIterator in range(0, len(lineOfSplit)):
                if lineOfSplit[0] == "\n":
                    break
                try:
                    element = int(lineOfSplit[columnIterator])
                    row.append(element)
                except ValueError as exc:
                    print(exc)
                    sys.exit(1)
            if len(row) != 0:
                self.matrix.append(row)
        file.close()

    @classmethod
    def add(cls, matrix1:Matrix(), matrix2:Matrix()):
        if len(matrix1)!=len(matrix2):
            raise IfMatrixAreNotSameSize('we can\'t add this two matrix(not same number of rows).')
        matrix = []
        for rowIterator in range(0, len(matrix1)):
            row = []
            for columnsIterator in range(0,matrix1.lenOfColumn(rowIterator)):
                if matrix1.lenOfColumn(rowIterator)!=matrix2.lenOfColumn(rowIterator):
                    raise IfMatrixAreNotSameSize('we can\'t add this two matrix(not same number of columns).')
                row.append(matrix1.elementRowCol(rowIterator, columnsIterator) + matrix2.elementRowCol(rowIterator, columnsIterator))
            matrix.append(row)
        return Matrix(matrix)

    def __add__(self, other):
        if (len(self.matrix) != len(other.matrix)):
            raise IfMatrixAreNotSameSize('we can\'t add this two matrix(not same number of rows).')
        matrix = []
        for rowIterator in range(0, len(self.matrix)):
            row = []
            for columIterator in range(0, len(self.matrix[rowIterator])):
                if (len(self.matrix[rowIterator]) != len(other.matrix[rowIterator])):
                    raise IfMatrixAreNotSameSize('we can\'t add this two matrix(not same number of columns).')
                row.append(self.matrix[rowIterator][columIterator] + other.matrix[rowIterator][columIterator])
            matrix.append(row)
        return Matrix(matrix)

    @classmethod
    def sub(cls, matrix1:Matrix(), matrix2:Matrix()):
        if len(matrix1)!=len(matrix2):
            raise IfMatrixAreNotSameSize('we can\'t add this two matrix(not same number of rows).')
        matrix = []
        for rowIterator in range(0, len(matrix1)):
            row = []
            for columnsIterator in range(0,matrix1.lenOfColumn(rowIterator)):
                if matrix1.lenOfColumn(rowIterator)!=matrix2.lenOfColumn(rowIterator):
                    raise IfMatrixAreNotSameSize('we can\'t add this two matrix(not same number of columns).')
                row.append(matrix1.elementRowCol(rowIterator, columnsIterator) - matrix2.elementRowCol(rowIterator, columnsIterator))
            matrix.append(row)
        return Matrix(matrix)

    def __sub__(self, other):
        if (len(self.matrix) != len(other.matrix)):
            raise IfMatrixAreNotSameSize('we can\'t subtract this two matrix(not same number of rows).')
        matrix = []
        for rowIterator in range(0, len(self.matrix)):
            row = []
            for columIterator in range(0, len(self.matrix[rowIterator])):
                if (len(self.matrix[rowIterator]) != len(other.matrix[rowIterator])):
                    raise IfMatrixAreNotSameSize('we can\'t subtract this two matrix(not same number of columns).')
                row.append(self.matrix[rowIterator][columIterator] - other.matrix[rowIterator][columIterator])
            matrix.append(row)
        return Matrix(matrix)

    @classmethod
    def showStatic(cls, matrix):
        if len(matrix) == 0:
            raise IfLengthIsZero('matrix size is zero.')
        for rowIterator in range (0, len(matrix)):
            print(matrix.elementRow(rowIterator))

    def show(self):
        if len(self.matrix) == 0:
            raise IfLengthIsZero('matrix size is zero.')
        for rowIterator in range (0, len(self.matrix)):
            print(self.matrix[rowIterator])

    @classmethod
    def fillFileWithMatrixStatic(cls, matrix, file):
        if len(matrix) == 0:
            raise IfLengthIsZero('matrix size is zero.')
        for rowIterator in range(0, len(matrix)):
            for columnIterator in range(0, len(matrix)):
                if matrix.lenOfColumn(rowIterator) - 1 == columnIterator:
                    file.write(str(matrix.elementRowCol(rowIterator, columnIterator)))
                    file.write("\n")
                else:
                    file.write(str(matrix.elementRowCol(rowIterator, columnIterator)))
                    file.write(",")

    def fillFileWithMatrix(self, file):
        if len(self.matrix) == 0:
            raise IfLengthIsZero('matrix size is zero.')
        for rowIterator in range(0, len(self.matrix)):
            for columnIterator in range(0, len(self.matrix)):
                if len(self.matrix[rowIterator]) - 1 == columnIterator:
                    file.write(str(self.matrix[rowIterator][columnIterator]))
                    file.write("\n")
                else:
                    file.write(str(self.matrix[rowIterator][columnIterator]))
                    file.write(",")