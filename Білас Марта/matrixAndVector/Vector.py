from Exceptions import *


class Vector:
    pass


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
        vector = []
        with open(fileName) as file:
            try:
                for line in file:
                    if (not line.isspace()):
                        line = line.split(" ")
                        for iterator in range(0, len(line)):
                            element = int(line[iterator])
                            vector.append(element)
            except ValueError:
                print("wrong element type")
                vector.clear()
        return Vector(vector)

    def printToFile(self, fileName):
        try:
            with open(fileName, "w") as file:
                if (self.vector == []):
                    raise Empty
                for i in range(0, len(self.vector)):
                    file.write(str(self.vector[i]) + " ")
        except Empty:
            print("vector is empty")

    @classmethod
    def staticPrintToFile(cls, fileName, vector):
        try:
            with open(fileName, "w") as file:
                if (vector == []):
                    raise Empty
                for i in range(0, len(vector)):
                    file.write(str(vector[i]) + " ")
        except Empty:
            print("vector is empty")

    def __add__(self, other):
        result = Vector()
        result.vector = []
        try:
            if (len(self.vector) != len(other.vector)):
                raise DifferentLength()
            for i in range(0, len(self.vector)):
                result.vector.append(self.vector[i] + other.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return result

    @classmethod
    def staticAdd(cls, firstVector=Vector(), secondVector=Vector()):
        result = []
        try:
            if (len(firstVector.vector) != len(secondVector.vector)):
                raise DifferentLength()
            for i in range(0, len(firstVector.vector)):
                result.append(firstVector.vector[i] + secondVector.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return cls(result)

    def __sub__(self, other):
        result = Vector()
        result.vector = []
        try:
            if (len(self.vector) != len(other.vector)):
                raise DifferentLength()
            for i in range(0, len(self.vector)):
                result.vector.append(self.vector[i] - other.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return result

    @classmethod
    def staticAdd(cls, firstVector=Vector(), secondVector=Vector()):
        result = []
        try:
            if (len(firstVector.vector) != len(secondVector.vector)):
                raise DifferentLength()
            for i in range(0, len(firstVector.vector)):
                result.append(firstVector.vector[i] - secondVector.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return cls(result)
