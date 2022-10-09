from lengthNotMatchExeption import LengthNotMatchExeption


class Vector:

    def __init__(self, vector=None):
        if vector is None:
            self.__vector = []
        else:
            self.__vector = vector

    def __mul__(self, other):
        suma = 0
        if len(self.__vector) == len(other.__vector):
            for iterator in range(len(self.__vector)):
                suma = suma + self.__vector[iterator] * other.__vector[iterator]
        return suma

    def __truediv__(self, other):
        vector = [round(self.__vector[i] / other.__vector[i],2) for i in range(len(self.__vector))]
        return Vector(vector)
    @classmethod
    def readFromFile(cls, nameFile=""):
        with open(nameFile, "r") as file:
            vector = []
            for line in file.readlines():
                for item in line.strip().split(","):
                    vector.append(item)
            vector = [item for item in vector if item]
            vector = [int(item) for item in vector if item]
        return cls(vector)

    def __str__(self):
        result = ""
        for item in self.__vector:
            result += str(item) + " "
        result += "\n"
        return result

    def __add__(self, other):
        vectorResult = Vector()
        if len(self.__vector) != len(other.__vector):
            raise LengthNotMatchExeption("Vector length not match")
        for item in range(len(self.__vector)):
            vectorResult.__vector.append(self.__vector[item] + other.__vector[item])
        return vectorResult

    def __sub__(self, other):
        vectorResult = Vector()
        if len(self.__vector) != len(other.__vector):
            raise LengthNotMatchExeption("Vector length not match")
        for item in range(len(self.__vector)):
            vectorResult.__vector.append(self.__vector[item] + other.__vector[item])
        return vectorResult

    def writeToFile(self, nameFile):
        with open(nameFile, "a") as file:
            file.write(str(self))

    @classmethod
    def sum_vector(cls, vectorFirst, vectorSecond):
        return cls(vectorFirst+vectorSecond)

    @classmethod
    def sub_vector(cls, vectorFirst, vectorSecond):
        return cls(vectorFirst+vectorSecond)

    def __len__(self):
        return len(self.__vector)

    def __getitem__(self, key):
        return self.__vector[key]