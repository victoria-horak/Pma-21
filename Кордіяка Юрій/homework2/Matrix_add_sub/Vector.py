from DifferentLengtException import DifferentLengthException


class Vector():
    def __init__(self, vector=None):
        if vector is None:
            vector = []
        self.__vector = vector

    def read_matrix(self, file_name):
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
        if len(self.__vector) == len(other.__vector):
            vector = [self.__vector[iterator] + other.__vector[iterator] for iterator in range(len(self.__vector))]
            return Vector(vector)
        else:
            raise DifferentLengthException('the lengths of the matrices do not match')

    def __sub__(self, other):
        if len(self.__vector) == len(other.__vector):
            vector = [self.__vector[iterator] - other.__vector[iterator] for iterator in range(len(self.__vector))]
            return Vector(vector)
        else:
            raise DifferentLengthException('the lengths of the matrices do not match')

    def __str__(self):
        return str(self.__vector)

    def write_to_file(self, file_name):
        with open(file_name, "a") as file:
            file.write(str(self.__vector))
            file.write('\n')
        file.close()
