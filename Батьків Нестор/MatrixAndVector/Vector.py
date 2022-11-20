import re
from diffrentDimensionsException import diffrentDimensionsException


class Vector:

    def __init__(self, inputValue=None, splitter=", "):
        self._string_splitter = splitter
        self.vector = inputValue or []

    def fromString(self, inputValue):
        self.fromList(re.sub("(^ )|( $)", "", re.sub(
            "\D+", " ", inputValue)).split(" "))

    def fromList(self, rawList):
        try:
            self._vector = [float(i) for i in rawList]
        except ValueError:
            raise ValueError("Element of Vector must be int!")

    @ property
    def splitter(self):
        return self._string_splitter

    @ splitter.setter
    def splitter(self, splitter: str):
        if not isinstance(splitter, str):
            raise TypeError("Splitter must be str")
        self._string_splitter = splitter

    def __str__(self):
        string = str(self._vector)
        string = re.sub("\[(.*)\]", r"(\1)", string)
        if self.splitter != ", ":
            string = re.sub(", ", self.splitter, string)
        return "\n" + string + "\n"

    @ property
    def length(self):
        return len(self._vector)

    @ property
    def vector(self):
        return self._vector

    @ vector.setter
    def vector(self, inputValue):
        if isinstance(inputValue, list):
            self.fromList(inputValue)
        if isinstance(inputValue, str):
            self.fromString(inputValue)

    @classmethod
    def fromFile(cls, filePath):
        with open(filePath, "r") as file:
            return cls(file.read())

    @ staticmethod
    def Convert(func):
        def inner(*args):
            args = list(args)
            if not isinstance(args[-1], Vector):
                args[-1] = Vector(args[-1])

            return func(*args)
        return inner

    def at(self, index):
        try:
            return self._vector[index]
        except IndexError as exc:
            return exc

    @ Convert
    def isSameLength(self, vector_b):
        return self.length == vector_b.length

    @staticmethod
    @ Convert
    def add(vector_first, vector_second):
        if not vector_first.isSameLength(vector_second):
            raise diffrentDimensionsException("Vectors have diffrent length")
        result = []
        for i in range(vector_first.length):
            result.append(vector_first.at(i) + vector_second.at(i))

        return Vector(result)

    def __add__(self, vector_second):
        return self.add(self, vector_second)

    @staticmethod
    @ Convert
    def sub(vector_first, vector_second):
        if not vector_first.isSameLength(vector_second):
            raise diffrentDimensionsException("Vectors have diffrent length")
        result = []
        for i in range(vector_first.length):
            result.append(vector_first.at(i) - vector_second.at(i))
        return Vector(result)

    def __sub__(self, vector_second):
        return self.sub(self, vector_second)

    def scalar_mult(self, mult):
        return Vector([int(i) * mult for i in self.vector])

    def __mul__(self, mult):
        if isinstance(mult, Vector):
            return self.multiply(self, mult)
        else:
            return self.scalar_mult(mult)

    def __truediv__(self, divisor):
        if isinstance(divisor, Vector):
            return self.divide(self, divisor)
        else:
            return self.scalar_mult(1/divisor)

    @staticmethod
    def toFile_Static(matrix, filePath, overwrite=False):
        with open(filePath, "w" if overwrite else "a") as file:
            file.write(str(matrix) + "\n")

    def toFile(self, filePath, overwrite=False):
        self.toFile_Static(self, filePath, overwrite)

    @staticmethod
    def divide(vector_first, vector_second):
        if not vector_first.isSameLength(vector_second):
            raise diffrentDimensionsException("Vectors have diffrent length")
        result = []
        for i in range(vector_first.length):
            result.append(vector_first.at(i) / vector_second.at(i))
        return Vector(result)

    @staticmethod
    def multiply(vector_first, vector_second):
        if not vector_first.isSameLength(vector_second):
            raise diffrentDimensionsException("Vectors have diffrent length")
        result = []
        for i in range(vector_first.length):
            result.append(vector_first.at(i) * vector_second.at(i))
        return Vector(result)
