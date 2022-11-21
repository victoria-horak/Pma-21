from LengthError import LengthErrorException
from ErrorDivision import ErrorDivision


class Vector:

    def __init__(self, vector):
        self.__vector = Vector.filling(self, vector)

    def filling(self, vector):
        if type(vector) is str:
            return Vector.readFromFile(self, vector)
        else:
            return vector

    def readFromFile(self, nameFile=""):
        with open(nameFile, "r") as file:
            vector = []
            for line in file.readlines():
                for item in line.strip().split(","):
                    vector.append(item)
            vector = [item for item in vector if item]
            vector = [int(item) for item in vector if item]
        return vector

    def __add__(self, other):
        if len(self.__vector) != len(other.__vector):
            raise LengthErrorException("vectors have different sizes\n")
        else:
            vector1 = [self.__vector[iterator] + other.__vector[iterator] for iterator in range(len(self.__vector))]
            return Vector(vector1)

    def __mul__(self, other):
        if len(self.__vector) != len(other.__vector):
            raise LengthErrorException("vectors have different sizes\n")
        else:
            result = 0
            for i in range(len(self.__vector)):
                result += self.__vector[i] * other.__vector[i]
            return result

    def __truediv__(self, number):
        if number == 0:
            raise ErrorDivision("division by 0")
        else:
            vector = [round(self.__vector[iterator] / number, 2) for iterator in range(len(self.__vector))]
            return Vector(vector)

    @classmethod
    def add_vectors(cls, vector1=None, vector2=None):
        if len(vector1) != len(vector2):
            raise LengthErrorException("vectors have different sizes\n")
        else:
            addedVector = [vector1[iterator] + vector2[iterator] for iterator in range(len(vector1))]
            return cls(addedVector)

    @classmethod
    def mult_vectors(cls, vector1=None, vector2=None):
        if len(vector1) != len(vector2):
            raise LengthErrorException("vectors have different sizes\n")
        else:
            multVector = [vector1[iterator] * vector2[iterator] for iterator in range(len(vector1))]
            return cls(multVector)

    @classmethod
    def division_vectors(cls, vector1=None, vector2=None):
        for itr in vector2:
            if itr == 0:
                raise ErrorDivision("division by 0")
        if len(vector1) != len(vector2):
            raise LengthErrorException("vectors have different sizes\n")
        else:
            devVector = [round(vector1[iterator] / vector2[iterator], 2) for iterator in range(len(vector1))]
            return cls(devVector)

    def __sub__(self, other):
        if len(self.__vector) != len(other.__vector):
            raise LengthErrorException("vectors have different sizes\n")
        else:
            vector = [self.__vector[iterator] - other.__vector[iterator] for iterator in range(len(self.__vector))]
            return Vector(vector)

    @classmethod
    def sub_vectors(cls, vector1=None, vector2=None):
        if len(vector1) != len(vector2):
            raise LengthErrorException("vectors have different sizes\n")
        else:
            subVector = [vector1[iterator] - vector2[iterator] for iterator in range(len(vector1))]
            return cls(subVector)

    def write_to_file(self, file_name):
        with open(file_name, 'a') as file:
            for iterator in self.__vector:
                file.write(str(iterator) + '\n')
            file.write('\n')

    def __str__(self):
        string = ''
        for iterator in self.__vector:
            string += str(iterator) + '\n'
        return string
