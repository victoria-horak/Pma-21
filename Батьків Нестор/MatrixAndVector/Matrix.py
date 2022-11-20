import re
from diffrentDimensionsException import diffrentDimensionsException
from NotValidListException import NotValidListException
from NotSquareMatrixException import NotSquareMatrixException
from ZeroDetException import ZeroDetException

class Matrix:

    def __init__(self, inputValue=None, splitter=", "):
        self._string_splitter = splitter
        self.matrix = inputValue or []

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
        string = re.sub(",", " ", string)
        string = re.sub("(\n|^)\s*", "\n", string)
        string = re.sub("(^ *\n)|(\n* *$)", "", string)
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
        #print(f"InputValue {input_value}")
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

    def det(self):
        if self.height == 2 and self.width == 2 :
            return self.at(0,0) * self.at(1,1) - self.at(0,1) * self.at(1,0)
        
        elif self.height == 3 and self.width == 3:
            return self.at(0,0) * self.at(1,1) * self.at(2,2) + self.at(1,0) * self.at(2,1) * self.at(0,2) + self.at(0,1) * self.at(1,2)*self.at(2,0) -\
            self.at(0,2) * self.at(1,1) * self.at(2,0) - self.at(0,1) * self.at(1,0) * self.at(2,2) - self.at(0,0) * self.at(1,2) * self.at(2,1)
        raise diffrentDimensionsException("Cant find determinant of matrix with such sides")
    
    def inverse(self):
        result = Matrix()
        determinant = self.det()
        if self.width != self.height:
                raise NotSquareMatrixException("matrix is not square")
        if determinant == 0:
            raise ZeroDetException("Cant inverse matrix with determinant 0")
        if len(self.matrix) == 2:
                result = Matrix.get_filled_matrix(2,2,0)
                result[0][0] = round(self[1][1]/determinant,2)
                result[0][1] = round((-1)*self[0][1] / determinant,2)
                result[1][0] = round((-1)*self[1][0] / determinant,2)
                result[1][1] = round(self[0][0] / determinant,2)
                return result
        if len(self.matrix) == 3:
                for i in range(3):
                    row = []
                    for j in range(3):
                        element = round(((self[(j + 1) % 3][(i + 1) % 3] * self[(j + 2) % 3][(i + 2) % 3]) - (
                                self[(j + 1) % 3][(i + 2) % 3] * self[(j + 2) % 3][
                            (i + 1) % 3])) / determinant,3)
                        row.append(element if element else 0 )
                    result.matrix.append(row)
                return result

        
        
    
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

    @staticmethod
    def multiply(matrix_a, matrix_b):
        if matrix_a.width != matrix_b.height:
            raise diffrentDimensionsException(
                "Matrix first with and matrix second height must be equal")
        newMatrix = []
        for i in range(matrix_a.height):
            newMatrix.append([0]*matrix_b.width)
            for j in range(matrix_b.width):
                for n in range(matrix_a.width):
                    newMatrix[i][j] = round(matrix_a.at(i, n) * \
                        matrix_b.at(n, j) + newMatrix[i][j],2)
        return Matrix(newMatrix)

    def __mul__(self, matrix_b):
        return Matrix.multiply(self, matrix_b)

    @staticmethod
    def get_filled_matrix(width, height, filler=0):
        return Matrix([[filler]*width for _ in range(height)])

    def set_value(self, x, y, value):
        # print(f"id1 {id(self._matrix[y])}")
        # print(f"id2 {id(self._matrix[y+1])}")

        self._matrix[x][y] = value
        return self

    @staticmethod
    def get_identity_matrix(width):
        new_matrix = Matrix.get_filled_matrix(width, width)
        for n in range(width):
            new_matrix.set_value(n, n, 1)
        return new_matrix

    @staticmethod
    @Convert
    def divide(matrix_a, matrix_b):
        return matrix_a * matrix_b.transpose

    def __getitem__(self,i):
        return self._matrix[i]
    def __truediv__(self, matrix_b):
        return Matrix.divide(self, matrix_b)
