from differentExceptions import *


class Vector:

    def __init__(self, vector=[]):
        if vector == []:
            self.vector = []
        elif type(vector) == int or type(vector) == float or type(vector) == chr or type(vector) == str:
            raise DifferentError('not vector')
        else:
            self.vector = vector

    def fillFromFile(self, fileName):
        file = open(fileName)
        lines = file.readlines()
        for rowIterator in range(0, len(lines)):
            if lines[rowIterator].isspace():
                continue
            line = lines[rowIterator].split(",")
            for columnsIterator in range(0, len(line)):
                try:
                    element = int(line[columnsIterator])
                    self.vector.append(element)
                except ValueError as exc:
                    print("Error: " + str(exc))
                    exit(0)
        file.close()

    @classmethod
    def fillFromFileStatic(self, fileName):
        vector = Vector()
        vector.fillFromFile(fileName)
        return vector

    def add(self, other):
        if len(self.vector) != len(other.vector):
            raise DifferentError('we can\'t add this two vectors(not same length).')
        vector = []
        for rowIterator in range(0, len(self.vector)):
            vector.append(self.vector[rowIterator] + other.vector[rowIterator])
        return Vector(vector)

    def __add__(self, other):
        return self.add(other)

    @classmethod
    def addStatic(cls, firstVector, secondVector):
        return firstVector.add(secondVector)

    def sub(self, other):
        if len(self.vector) != len(other.vector):
            raise DifferentError('we can\'t add this two vectors(not same length).')
        vector = []
        for rowIterator in range(0, len(self.vector)):
            vector.append(self.vector[rowIterator] - other.vector[rowIterator])
        return Vector(vector)

    @classmethod
    def subStatic(cls, firstVector, secondVector):
        return firstVector.sub(secondVector)

    def __sub__(self, other):
        return self.sub(other)

    def show(self):
        if len(self.vector) == 0:
            raise DifferentError('vector size is 0.')
        print(self.vector)

    @classmethod
    def showStatic(cls, vector):
        vector.show()

    def fillFileWithVector(self, file):
        if len(self.vector) == 0:
            raise DifferentError('vector size is 0.')
        file.write(str(self.vector))
        file.write("\n")

    @classmethod
    def fillFileWithVectorStatic(cls, vector, file):
        vector.fillFileWithVector(file)

    def multiplication(self, other):
        if len(self.vector) != len(other.vector):
            raise DifferentError('vectors are not same size, we cant multiplicate them.')
        result = 0
        for iterator in range(len(self.vector)):
            result += self.vector[iterator] * other.vector[iterator]
        return result

    def __mul__(self, other):
        return self.multiplication(other)

    @classmethod
    def multiplicationStatic(cls, matrix1, matrix2):
        return matrix1.multiplicate(matrix2)

    def division(self, other):
        if len(self.vector) != len(other.vector):
            raise DifferentError('vectors are different sizes, we cannot divide them.')
        resultVector = Vector()
        for iterator in range(len(self.vector)):
            resultVector.vector.append(self.vector[iterator] / other.vector[iterator])
        return resultVector

    def __truediv__(self, other):
        return self.division(other)

    @classmethod
    def divisionStatic(cls, matrix1, matrix2):
        return matrix1.division(matrix2)
