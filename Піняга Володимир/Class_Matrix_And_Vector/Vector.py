from differLength import *

class Vector():
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


    def __str__(self):
        return str(self.vector)


    def write(self, fileName):
        f = open(fileName, "a")
        f.write(str(self.vector))
        f.write('\n')
        f.close()



    def substract_2_vectors(self, second): #віднімання 2 векторів
        if (len(self.vector) == len(second.vector)):
            res_vector = Vector(self.len_vector) #утворення результуючого вектора
            res_vector.vector = []
            for iter in range(0, self.len_vector and second.len_vector):
                res_vector.vector.append(int(self.vector[iter]) - int(second.vector[iter]))

        else:
            res_vector = Vector(self.len_vector)
            res_vector.vector = []  # утворення результуючого вектора
            print("Vectors cannot be added")

        return res_vector
