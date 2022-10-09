from Exceptions.DifferentLengtException import DifferentLengthException


class Vector():
    def __init__(self, vector):
        if type(vector) is list:
            self.__vector = vector
        elif type(vector) is str:
            self.__vector = Vector.read_vector_from_file(self, vector)

    def read_vector_from_file(self, file_name):
        with open(file_name, "r") as file:
            list_for_vector = []
            for line in file:
                for x in line.strip().split(','):
                    list_for_vector.append(x)
            list_for_vector = [x for x in list_for_vector if x]
            list_for_vector = [int(x) for x in list_for_vector if x]
        return list_for_vector

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

    @classmethod
    def read_vector_static(cls, file_name):
        with open(file_name, "r") as file:
            list_for_vector = []
            for line in file:
                for x in line.strip().split(','):
                    list_for_vector.append(x)
            list_for_vector = [x for x in list_for_vector if x]
            list_for_vector = [int(x) for x in list_for_vector if x]
        return cls(list_for_vector)

    def __add__(self, other):
        if len(self.__vector) == len(other.__vector):
            vector = [self.__vector[iterator] + other.__vector[iterator] for iterator in range(len(self.__vector))]
            return Vector(vector)
        else:
            raise DifferentLengthException('the lengths of the matrices do not match')

    def __len__(self):
        return len(self.__vector)

    def __getitem__(self, index):
        return self.__vector[index]

    @classmethod
    def add_vector_static(cls, vector1, vector2):
        return cls(vector1 + vector2)

    def __sub__(self, other):
        if len(self.__vector) == len(other.__vector):
            vector = [self.__vector[iterator] - other.__vector[iterator] for iterator in range(len(self.__vector))]
            return Vector(vector)
        else:
            raise DifferentLengthException('the lengths of the matrices do not match')

    def __mul__(self, other):
        suma = 0
        if len(self.__vector) == len(other.__vector):
            for iterator in range(len(self.__vector)):
                suma = suma + self.__vector[iterator] * other.__vector[iterator]
        return suma

    def mul_to_scalar(self, scalar):
        self.__vector = [scalar * self.__vector[iterator] for iterator in range(len(self.__vector))]
        return self.__vector

    def __truediv__(self, other):
        vector = [self.__vector[i] / other.__vector[i] for i in range(len(self.__vector))]
        return Vector(vector)

    @classmethod
    def sub_vector_static(cls, vector1, vector2):
        return cls(vector1 - vector2)

    def __str__(self):
        return str(self.__vector)

    def write_to_file(self, file_name):
        with open(file_name, "a") as file:
            file.write(str(self.__vector))
            file.write("\n")
        file.close()

    @classmethod
    def write_to_file_static(cls, file_name, vector):
        with open(file_name, "a") as file:
            file.write(str(vector))
            file.write("\n")
        file.close()
