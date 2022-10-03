from differentExceptions import *


class Matrix:
    def __init__(self, matrix=[]):
        self.matrix = []
        if type(matrix) == int or type(matrix) == float or type(matrix) == chr or type(matrix) == str:
            raise DifferentError('not matrix')
        elif matrix != []:
            self.matrix = matrix

    def fillConsole(self):
        try:
            lengthRows = int(input("Enter length of rows: "))
            lengthColumns = int(input("Enter length of columns: "))
        except ValueError as exc:
            print("Error" + str(exc))
            exit()
        for rowIterator in range(0, lengthRows):
            row = []
            for columnIterator in range(0, lengthColumns):
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
            for columnIterator in range(0, len(lineOfSplit)):
                try:
                    element = int(lineOfSplit[columnIterator])
                    row.append(element)
                except ValueError as exc:
                    print(exc)
                    exit(0)
                except IndexError as exc:
                    print(exc)
                    exit(0)
            if len(row) != 0:
                self.matrix.append(row)
        file.close()

    def add(self, other):
        if (len(self.matrix) != len(other.matrix)):
            raise DifferentError('we can\'t add this two matrix(not same number of rows).')
        matrix = []
        for rowIterator in range(0, len(self.matrix)):
            row = []
            for columIterator in range(0, len(self.matrix[rowIterator])):
                if (len(self.matrix[rowIterator]) != len(other.matrix[rowIterator])):
                    raise DifferentError('we can\'t add this two matrix(not same number of columns).')
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
        matrix = []
        for rowIterator in range(0, len(self.matrix)):
            row = []
            for columIterator in range(0, len(self.matrix[rowIterator])):
                if (len(self.matrix[rowIterator]) != len(other.matrix[rowIterator])):
                    raise DifferentError('we can\'t subtract this two matrix(not same number of columns).')
                row.append(self.matrix[rowIterator][columIterator] - other.matrix[rowIterator][columIterator])
            matrix.append(row)
        return Matrix(matrix)

    def __sub__(self, other):
        return self.sub(other)

    @classmethod
    def subStatic(cls, matrix1, matrix2):
        return matrix1.sub(matrix2)

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
