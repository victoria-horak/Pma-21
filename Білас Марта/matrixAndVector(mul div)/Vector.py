from Exceptions import *


class Vector:

    def init(self, vector=[]):
        try:
            self.vector = vector
        except ValueError:
            print("value error")
        pass

    def readFromFile(self, fileName):
        self.vector = []
        with open(fileName) as file:
            try:
                for line in file:
                    if (not line.isspace()):
                        line = line.split(",")
                        for iterator in range(0, len(line)):
                            element = int(line[iterator])
                            self.vector.append(element)
            except ValueError:
                print("wrong element type")

    @classmethod
    def staticReadFromFile(cls, fileName):
        result = Vector()
        result.readFromFile(fileName)
        return result

    def printToFile(self, fileName):
        try:
            with open(fileName, "w") as file:
                if self.vector == []:
                    raise Empty
                for i in range(0, len(self.vector)):
                    file.write(str(self.vector[i]) + " ")
        except Empty:
            print("vector is empty")

    @classmethod
    def staticPrintToFile(cls, fileName, vector):
        vector.printToFile(fileName)

    def __add__(self, other):
        result = Vector()
        result.vector = []
        try:
            if len(self.vector) != len(other.vector):
                raise DifferentLength()
            for i in range(0, len(self.vector)):
                result.vector.append(self.vector[i] + other.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return result

    @classmethod
    def staticAdd(cls, firstVector, secondVector):
        result = Vector()
        result = firstVector + secondVector
        return result

    def __sub__(self, other):
        result = Vector()
        result.vector = []
        try:
            if len(self.vector) != len(other.vector):
                raise DifferentLength()
            for i in range(0, len(self.vector)):
                result.vector.append(self.vector[i] - other.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return result

    @classmethod
    def staticSub(cls, firstVector, secondVector):
        result = Vector()
        result = firstVector - secondVector
        return result

    def __truediv__(self, other):
        result = Vector()
        result.vector = []
        try:
            if len(self.vector) != len(other.vector):
                raise DifferentLength()
            for i in range(0, len(self.vector)):
                result.vector.append(self.vector[i] / other.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return result

    @classmethod
    def staticDivision(cls, firstVector, secondVector):
        result = Vector()
        result = firstVector / secondVector
        return result

    def __mul__(self, other):
        result = 0
        try:
            if len(self.vector) != len(other.vector):
                raise DifferentLength()
            for i in range(0, len(self.vector)):
                element = self.vector[i] * other.vector[i]
                result += element
        except DifferentLength:
            print("vectors have different length")
        return result

    @classmethod
    def staticMultiplication(cls, firstVector, secondVector):
        result = firstVector * secondVector
        return result
