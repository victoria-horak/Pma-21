from DifferentSizesVectors import *


class Vector():
    def __init__(self, vector):
        """Ініціалізація вектору"""
        self.vector = vector

    def read_vector(self, file_name):
        """Зчитування вектору з файлу"""
        with open(file_name, "r") as file:
            vector_as_row = []
            for line in file:
                for element in line.strip().split(','):
                    vector_as_row.append(element)
            vector_as_row = [element for element in vector_as_row if element]
            vector_as_row = [int(element) for element in vector_as_row if element]
            self.vector = vector_as_row
        file.close()
        return self.vector

    def __add__(self, other):
        """Додавання векторів"""
        if len(self.vector) == len(other.vector):
            vector = [self.vector[iterator] + other.vector[iterator] for iterator in range(len(self.vector))]
            return Vector(vector)
        else:
            raise DifferentSizesVectors('Vectors have different sizes')

    def __sub__(self, other):
        """Віднімання векторів"""
        if len(self.vector) == len(other.vector):
            vector = [self.vector[iterator] - other.vector[iterator] for iterator in range(len(self.vector))]
            return Vector(vector)
        else:
            raise DifferentSizesVectors('Vectors have different sizes')

    def __str__(self):
        """Перетворення вектора в стрічку для виводу"""
        return str(self.vector)

    def write_to_file(self, file_name):
        """Вивід в файл"""
        file = open(file_name, "a")
        file.write(str(self.vector))
        file.write('\n')
        file.close()
