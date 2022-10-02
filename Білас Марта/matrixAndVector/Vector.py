from Exceptions import *


class Vector:
    pass


class Vector:

    def __init__(self, vector:int=None):
        try:
            if (vector is None):
                self.vector = []
            else:
                self.vector = vector
        except ValueError:
            print("value error")
        pass

    def readFromFile(self, fileName):
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
                self.vector.clear()

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
        try:
            if (len(self.vector) != len(other.vector)):
                raise DifferentLength()
            for i in range(0, len(self.vector)):
                result.vector.append(self.vector[i] + other.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return result

    @classmethod
    def staticAdd(cls, vector1=Vector(), vector2=Vector()):
        result = []
        try:
            if (len(vector1.vector) != len(vector2.vector)):
                raise DifferentLength()
            for i in range(0, len(vector1.vector)):
                result.append(vector1.vector[i] + vector2.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return cls(result)

    def __sub__(self, other):
        result = Vector()
        try:
            if (len(self.vector) != len(other.vector)):
                raise DifferentLength()
            for i in range(0, len(self.vector)):
                result.vector.append(self.vector[i] - other.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return result

    @classmethod
    def staticAdd(cls, vector1=Vector(), vector2=Vector()):
        result = []
        try:
            if (len(vector1.vector) != len(vector2.vector)):
                raise DifferentLength()
            for i in range(0, len(vector1.vector)):
                result.append(vector1.vector[i] - vector2.vector[i])
        except DifferentLength:
            print("vectors have different length")
        return cls(result)
