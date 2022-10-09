from DifferentSizesVectors import *

class Vector():
    def __init__(self, vector):
        """Ініціалізація вектору"""
        self.vector = vector

    def __str__(self):
        """Перетворення вектора в стрічку для виводу"""
        return str(self.vector)

    def __mul__(self, other):
        """Множення векторів"""
        if len(self.vector) == len(other.vector):
            mul_result = 0
            for iterator in range(len(self.vector)):
                mul_result += self.vector[iterator] * other.vector[iterator]
            return Vector(mul_result)
        else:
            raise DifferentSizesVectors("Vectors have different sizes")

    def __truediv__(self, other):
        """Ділення векторів"""
        if len(self.vector) == len(other.vector):
            vector = [self.vector[iterator] / other.vector[iterator] for iterator in range(len(self.vector))]
            for i in range(len(self.vector)):
                vector[i] = round(vector[i], 2)
            return Vector(vector)
        else:
            raise DifferentSizesVectors("Vectors have different sizes")

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

    def write_to_file(self, file_name):
        """Вивід в файл"""
        file = open(file_name, "a")
        file.write(str(self.vector))
        file.write('\n')
        file.close()
