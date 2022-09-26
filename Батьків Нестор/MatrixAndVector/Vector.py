import re
from diffrentDimensionsException import diffrentDimensionsException


class Vector:

    def __init__(self, inputValue=[], splitter=", "):
        self._string_splitter = splitter
        self.vector = inputValue

    def fromString(self, inputValue):
        self.fromList(re.sub("(^ )|( $)", "", re.sub(
            "\D+", " ", inputValue)).split(" "))

    def fromList(self, rawList):
        self._vector = [int(i) for i in rawList]

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
        return string

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

    @ Convert
    def __add__(self, vector_2):
        if not self.isSameLength(vector_2):
            raise diffrentDimensionsException("Vectors have diffrent length")
        result = []
        for i in range(self.length):
            result.append(self.at(i) + vector_2.at(i))

        return Vector(result)

    @ Convert
    def __sub__(self, vector_2):
        if not self.isSameLength(vector_2):
            raise diffrentDimensionsException("Vectors have diffrent length")
        result = []
        for i in range(self.length):
            result.append(self.at(i) - vector_2.at(i))

        return Vector(result)

    def scalar_mult(self, mult):
        return Vector([int(i) * mult for i in self.vector])

    def toFile(self, filePath, overwrite=True):
        with open(filePath, "w" if overwrite else "a") as file:
            file.write(str(self) + "\n")
