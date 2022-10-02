from Exceptions import *


class Matrix:
    pass


class Matrix:

    def __init__(self, matrix:int=None):
        try:
            if (matrix is None):
                self.matrix = []
            else:
                self.matrix = matrix
        except ValueError:
            print("value error")
        pass

    def readFromFile(self, fileName):
        with open(fileName) as file:
            try:
                for line in file:
                    if (not line.isspace()):
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
        matrix = []
        with open(fileName) as file:
            try:
                for line in file:
                    if (not line.isspace()):
                        line = line.split(",")
                        row = []
                        for columnIterator in range(0, len(line)):
                            element = int(line[columnIterator])
                            row.append(element)
                        matrix.append(row)
            except ValueError:
                print("wrong element type")
                matrix.clear()
        return cls(matrix)

    def printToFile(self, fileName):
        try:
            with open(fileName, "w") as file:
                if (self.matrix == []):
                    raise Empty
                for i in range(0, len(self.matrix)):
                    file.write(str(self.matrix[i]) + " ")
                    file.write('\n')
        except Empty:
            print("vector is empty")

    @classmethod
    def staticPrintToFile(cls, matrix, fileName):
        try:
            with open(fileName, "w") as file:
                if (matrix == []):
                    raise Empty
                for i in range(0, len(matrix)):
                    file.write(str(matrix[i]) + " ")
                    file.write('\n')
        except Empty:
            print("matrix is empty")

    def __add__(self, other):
        result = Matrix()
        rowLengthSelf = len(self.matrix)
        colonLengthSelf = len(self.matrix[0])
        rowLengthOther = len(other.matrix)
        colonLengthOther = len(other.matrix[0])
        try:
            if (rowLengthOther != rowLengthSelf or colonLengthSelf != colonLengthOther):
                raise DifferentLength()
            for rowIterator in range(0, rowLengthSelf):
                row = []
                for columnIterator in range(0, colonLengthSelf):
                    element = self.matrix[rowIterator][columnIterator] + other.matrix[rowIterator][columnIterator]
                    row.append(element)
                result.matrix.append(row)
        except DifferentLength:
            print("matrixes have different length")
        return result

    def length(self):
        return len(self.matrix)

    def at(self, rowIterator, columnIterator):
        return self.matrix[rowIterator][columnIterator]

    @classmethod
    def staticAdd(cls, matrix_a=Matrix(), matrix_b=Matrix()):

        result = []
        rowLengthSelf = matrix_a.length()
        rowLengthOther = matrix_b.length()

        try:
            if (rowLengthOther != rowLengthSelf):
                raise DifferentLength()
            for rowIterator in range(0, rowLengthSelf):
                row = []
                for columnIterator in range(0, rowLengthSelf):
                    element = matrix_a.at(rowIterator, columnIterator) + matrix_b.at(rowIterator, columnIterator)
                    row.append(element)
                result.append(row)
        except DifferentLength:
            print("matrixes have different length")
        return Matrix(result)

    def __sub__(self, other):
        result = Matrix()
        rowLengthSelf = len(self.matrix)
        colonLengthSelf = len(self.matrix[0])
        rowLengthOther = len(other.matrix)
        colonLengthOther = len(other.matrix[0])

        try:
            if (rowLengthOther != rowLengthSelf or colonLengthSelf != colonLengthOther):
                raise DifferentLength()
            for rowIterator in range(0, rowLengthSelf):
                row = []
                for columnIterator in range(0, colonLengthSelf):
                    element = self.matrix[rowIterator][columnIterator] - other.matrix[rowIterator][columnIterator]
                    row.append(element)
                result.matrix.append(row)
        except DifferentLength:
            print("matrixes have different length")
        return result

    @classmethod
    def staticSub(cls, matrix_a=Matrix(), matrix_b=Matrix()):

        result = []
        rowLengthSelf = matrix_a.length()
        rowLengthOther = matrix_b.length()

        try:
            if (rowLengthOther != rowLengthSelf):
                raise DifferentLength()
            for rowIterator in range(0, rowLengthSelf):
                row = []
                for columnIterator in range(0, rowLengthSelf):
                    element = matrix_a.at(rowIterator, columnIterator) - matrix_b.at(rowIterator, columnIterator)
                    row.append(element)
                result.append(row)
        except DifferentLength:
            print("matrixes have different length")
        return Matrix(result)
