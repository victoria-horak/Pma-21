import re
from diffrentDimensionsException import diffrentDimensionsException
from NotValidListException import NotValidListException


class Matrix:

    def __init__(self, inputValue=[], splitter=", "):
        self._string_splitter = splitter
        self.matrix = inputValue

    def isEmpty(self):
        return len(self._matrix) == 0

    @property
    def height(self):
        return len(self._matrix)

    @property
    def width(self):
        return 0 if self.isEmpty() else len(self._matrix[0])

    def at(self, row, column=0):
        try:
            return self._matrix[row][column]
        except IndexError as exc:
            return exc

    def fromList(self, _list, height=1):

        length = len(_list) / height
        matrix = []
        iterator = 0
        row = []
        for element in _list:
            try:
                row.append(int(element))
                iterator += 1
                if iterator >= length:
                    iterator = 0
                    matrix.append(row)
                    row = []
            except ValueError:
                raise ValueError("matrix element is not int")

        return matrix

    def fromString(self, string):
        string = re.sub("(\n|^)\s*", "\n", string)
        string = re.sub("(^ *\n)|(\n *$)", "", string)
        height = string.count("\n") + 1
        read_list = re.sub("\s+", " ", string).split(" ")
        return self.fromList(read_list, height)

    @staticmethod
    def Convert(func):
        def inner(*args):
            args = list(args)
            if not isinstance(args[-1], Matrix):
                args[-1] = Matrix(args[-1])

            return func(*args)
        return inner

    @staticmethod
    def isMatrix(input_matrix):
        try:
            return isinstance(input_matrix, list) and isinstance(input_matrix[0], list) and not isinstance(input_matrix[0][0], list)
        except IndexError:
            return False

    @ property
    def matrix(self):
        return self._matrix

    @ matrix.setter
    def matrix(self, input_value):
        if isinstance(input_value, str):
            self._matrix = self.fromString(input_value)
        elif isinstance(input_value, list):
            if self.isMatrix(input_value):
                self._matrix = input_value
            else:
                if len(input_value) > 0 and isinstance(input_value[0], list):
                    raise NotValidListException(
                        "Input list is not matrix or list of charactes")
                self._matrix = self.fromList(input_value)

    @property
    def splitter(self):
        return self._string_splitter

    @splitter.setter
    def splitter(self, splitter: str):
        if not isinstance(splitter, str):
            raise TypeError("Splitter must be str")
        self._string_splitter = splitter

    def __str__(self):
        string = str(self._matrix)
        string = re.sub("'|[\[\]]{2}", "", string)
        if self.splitter != ", ":
            string = re.sub(", ", self.splitter+"\t", string)
        string = re.sub("\].*?\[", "\n", string)
        string = "\n" + string + "\n"
        return string

    @property
    def transpose(self):
        newMatrix = []
        for column in range(self.width):
            newMatrix.append([])
            for row in range(self.height):
                newMatrix[column].append(self.at(row, column))
        return Matrix(newMatrix)

    @Convert
    def isSameDimensions(self, matrix):
        return self.width == matrix.width and self.height == matrix.height

    @staticmethod
    @Convert
    def add(matrix_a, matrix_b):
        if not matrix_a.isSameDimensions(matrix_b):
            raise diffrentDimensionsException("Matrixes have diffrent sizes")
        newMatrix = []
        for row in range(matrix_a.height):
            newMatrix.append([])
            for col in range(matrix_a.width):
                newMatrix[row].append(
                    matrix_a.at(row, col) + matrix_b.at(row, col))
        return Matrix(newMatrix)

    def __add__(self, matrix):
        return self.add(self, matrix)

    @staticmethod
    @Convert
    def sub(matrix_a, matrix_b):
        if not matrix_a.isSameDimensions(matrix_b):
            raise diffrentDimensionsException("Matrixes have diffrent sizes")
        newMatrix = []
        for row in range(matrix_a.height):
            newMatrix.append([])
            for col in range(matrix_a.width):
                newMatrix[row].append(
                    matrix_a.at(row, col) - matrix_b.at(row, col))
        return Matrix(newMatrix)

    def __sub__(self, matrix_b):
        return self.sub(self, matrix_b)

    def scalar_mult(self, multiplier):
        newMatrix = []
        for row in range(self.height):
            newMatrix.append([])
            for col in range(self.width):
                newMatrix[row].append(self.at(row, col) * multiplier)
        return Matrix(newMatrix)

    def subMatrix(self, row=-1, col=-1):
        matrix = self._matrix.copy()
        matrix.pop(row)
        for _row in matrix:
            _row.pop(col)
        return Matrix(matrix)

    @classmethod
    def fromFile(cls, filePath):
        with open(filePath, "r") as file:
            return cls(file.read())

    @staticmethod
    def toFile_Static(matrix, filePath, overwrite=False):
        with open(filePath, "w" if overwrite else "a") as file:
            file.write(str(matrix) + "\n")

    def toFile(self, filePath, overwrite=False):
        self.toFile_Static(self, filePath, overwrite)
