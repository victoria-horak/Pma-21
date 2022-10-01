from DifferentLengtException import DifferentLengthException


class Vector():
    def __init__(self,vector=None):
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
        if len(vector1) == len(vector2):
            result = [vector1[iterator] + vector2[iterator] for iterator in range(len(vector1))]
            return cls(result)
        else:
            raise DifferentLengthException('the lengths of the matrices do not match')

    def __sub__(self, other):
        if len(self.__vector) == len(other.__vector):
            vector = [self.__vector[iterator] - other.__vector[iterator] for iterator in range(len(self.__vector))]
            return Vector(vector)
        else:
            raise DifferentLengthException('the lengths of the matrices do not match')

    @classmethod
    def sub_vector_static(cls, vector1, vector2):
        if len(vector1) == len(vector2):
            result = [vector1[iterator] - vector2[iterator] for iterator in range(len(vector1))]
            return cls(result)
        else:
            raise DifferentLengthException('the lengths of the matrices do not match')

    def __str__(self):
        return str(self.__vector)

    def write_to_file(self, file_name):
        with open(file_name, "a") as file:
            file.write(str(self.__vector))
            file.write('\n')
        file.close()

    @classmethod
    def write_to_file_static(cls, file_name, vector):
        with open(file_name, "a") as file:
            file.write(str(vector))
            file.write('\n')
        file.close()
