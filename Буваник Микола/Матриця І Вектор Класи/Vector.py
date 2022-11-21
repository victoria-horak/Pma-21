from lengthNotMatchExeption import LengthNotMatchExeption


class Vector:

    def __init__(self, vector=None):
        self.__vector = Vector.filling(self, vector)

    def filling(self, vector):
        if type(vector) is str:
            return Vector.readFromFile(self, vector)
        else:
            return vector

    def __mul__(self, other):
        if len(self.__vector) == len(other.__vector):
            scalar = 0
            for iterator in range(len(self.__vector)):
                scalar += self.__vector[iterator] * other.__vector[iterator]
            scalar = [int(scalar)]
            return Vector(scalar)
        else:
            raise LengthNotMatchExeption("Vector have different length")

    def __truediv__(self, other):
        if len(self.__vector) == len(other.__vector):
            vector = []
            for iterator in range(len(self.__vector)):
                vector.append(round(self.__vector[iterator] / other.__vector[iterator], 2))
            return Vector(vector)
        else:
            raise LengthNotMatchExeption("Vector have different length")

    def readFromFile(self, nameFile=""):
        with open(nameFile, "r") as file:
            vector = []
            for line in file.readlines():
                for item in line.strip().split(","):
                    vector.append(item)
            vector = [item for item in vector if item]
            vector = [int(item) for item in vector if item]
        return vector

    def __str__(self):
        result = ""
        for item in self.__vector:
            result += str(item) + " "
        result += "\n"
        return result

    def __add__(self, other):
        if len(self.__vector) == len(other.__vector):
            vector = []
            for iterator in range(len(self.__vector)):
                vector.append(self.__vector[iterator] + other.__vector[iterator])
            return Vector(vector)
        else:
            raise LengthNotMatchExeption("Vector have different length")

    def __sub__(self, other):
        if len(self.__vector) == len(other.__vector):
            vector = []
            for iterator in range(len(self.__vector)):
                vector.append(self.__vector[iterator] - other.__vector[iterator])
            return Vector(vector)
        else:
            raise LengthNotMatchExeption("Vector have different length")

    def writeToFile(self, nameFile):
        with open(nameFile, "a") as file:
            file.write(str(self))

    @classmethod
    def sum_vector(cls, vectorFirst, vectorSecond):
        return cls(vectorFirst + vectorSecond)

    @classmethod
    def sub_vector(cls, vectorFirst, vectorSecond):
        return cls(vectorFirst - vectorSecond)

    def __len__(self):
        return len(self.__vector)

    def __getitem__(self, key):
        return self.__vector[key]
