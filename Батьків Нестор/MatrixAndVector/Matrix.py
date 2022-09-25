import re
from diffrentDimensionsException import diffrentDimensionsException
from NotValidListException import NotValidListException


class Matrix:

    def __init__(self, inputValue=[], splitter=", ", fileName=""):
        print(fileName)
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
            row.append(int(element))
            iterator += 1
            if iterator >= length:
                iterator = 0
                matrix.append(row)
                row = []

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
            string = re.sub(", ", self.splitter, string)
        string = re.sub("\].*?\[", "\n", string)
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

    @Convert
    def __add__(self, matrix):
        if not self.isSameDimensions(matrix):
            raise diffrentDimensionsException("Matrixes have diffrent sizes")
        newMatrix = []
        for row in range(self.height):
            newMatrix.append([])
            for col in range(self.width):
                newMatrix[row].append(
                    self.at(row, col) + matrix.at(row, col))
        return Matrix(newMatrix)

    def scalar_mult(self, multiplier):
        newMatrix = []
        for row in range(self.height):
            newMatrix.append([])
            for col in range(self.width):
                newMatrix[row].append(self.at(row, col) * multiplier)
        return Matrix(newMatrix)

    def __sub__(self, row=-1, col=-1):
        matrix = self._matrix.copy()
        matrix.pop(row)
        for _row in matrix:
            _row.pop(col)
        return Matrix(matrix)

    # Alias
    add = __add__
    sub = __sub__

    def fromFile(self, filePath):
        with open(filePath, "r") as file:
            self.matrix = file.read()
        return self
