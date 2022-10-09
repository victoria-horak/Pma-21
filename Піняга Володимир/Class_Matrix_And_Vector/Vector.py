from differLength import *


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def read_vector(self, file_name):
        with open(file_name, "r") as file:
            row_vector = []
            for line in file:
                for element in line.strip().split(','):
                    row_vector.append(element)
            row_vector = [element for element in row_vector if element]
            row_vector = [int(element) for element in row_vector if element]
            self.vector = row_vector
        file.close()
        return self.vector

    def write(self, file_name):
        f = open(file_name, "a")
        f.write(str(self.vector))
        f.write('\n')
        f.close()

    def __str__(self):
        return str(self.vector)

    def __add__(self, other):
        if len(self.vector) == len(other.vector):
            vector = [self.vector[iter] + other.vector[iter] for iter in range(len(self.vector))]
            return Vector(vector)
        else:
            raise differLength('Vectors don`t have the same size! ')

    def __sub__(self, other):
        if len(self.vector) == len(other.vector):
            vector = [self.vector[iter] - other.vector[iter] for iter in range(len(self.vector))]
            return Vector(vector)
        else:
            raise differLength('Vectors don`t have the same size! ')

    def __mul__(self, other):
        if len(self.vector) == len(other.vector):
            vector = [self.vector[iterator] * other.vector[iterator] for iterator in range(len(self.vector))]
            return Vector(vector)
        else:
            raise InvalidDimensionsForMatrixMultiplication("\nMatrices don`t have the valid size for "
                                                           "multiplication!")

    def __truediv__(self, other):
        try:
            if len(self.vector) == len(other.vector):
                vector = [self.vector[iterator] / other.vector[iterator] for iterator in range(len(self.vector))]
                return Vector(vector)
            else:
                raise differLength('Vectors don`t have the same size! ')
        except ZeroDivisionError:
            with open('result_vector.txt', "a+") as vector_file:
                vector_file.write("We cannot divide by zero!")
            return Vector([])

    @classmethod
    def add_vectors(cls, first: "Vector", second: "Vector") -> "Vector":
        return first + second

    @classmethod
    def subtract_vectors(cls, first: "Vector", second: "Vector") -> "Vector":
        return first - second

    @classmethod
    def multiply_vectors(cls, first: "Vector", second: "Vector") -> "Vector":
        return first * second

    @classmethod
    def divide_vectors(cls, first: "Vector", second: "Vector") -> "Vector":
        return first / second


