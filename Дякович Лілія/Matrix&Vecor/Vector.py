from LengthError import LengthErrorException


class Vector:
    def __init__(self, vector=None):
        if vector is None:
            vector = []
        self.__vector = vector

    def read_vector(self, file_name):
        with open(file_name, "r") as file:
            list_for_vector = []
            for line in file:
                for x in line.strip().split(','):
                    list_for_vector.append(x)
            list_for_vector = [x for x in list_for_vector if x]
            list_for_vector = [int(x) for x in list_for_vector if x]
            self.__vector = list_for_vector
        return self.__vector

    def __add__(self, other):
        if len(self.__vector) != len(other.__vector):
            raise LengthErrorException("vectors have different sizes\n")
        else:
            vector = [self.__vector[iterator] + other.__vector[iterator] for iterator in range(len(self.__vector))]
            return Vector(vector)

    @classmethod
    def add_vectors(cls, vector1=None, vector2=None):
        if len(vector1) != len(vector2):
            raise LengthErrorException("vectors have different sizes\n")
        else:
            addedVector = [vector1[iterator] + vector2[iterator] for iterator in range(len(vector1))]
            return cls(addedVector)

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
