from Exception import *


class Vector:
    def __init__(self, number):
        self.vector = [[0] * number]

    def set_vector(self, vector_first):
        self.vector = vector_first
        return self.vector

    def read_vector(self, name_of_file):
        file = open(name_of_file, 'r')
        vector_first = []
        read_text = file.read().replace('\n', ' ')
        elements = read_text.split()
        for i in range(len(elements)):
            vector_first.append(int(elements[i])), read_text[i].split()
        file.close()

        self.vector = vector_first

    def add_vector(self, second):
        if (len(self.vector) != len(second.vector)):
            raise DifferentSize("The vectors have different sizes")
        vector_result = Vector(len(self.vector))
        vector_add = [0] * len(self.vector)
        for i in range(len(self.vector)):
            vector_add[i] = self.vector[i] + second.vector[i]
        vector_result.set_vector(vector_add)
        return vector_result

    def __add__(self, second):
        if (len(self.vector) != len(second.vector)):
            raise DifferentSize("The vectors have different sizes \n")
        vector_result = Vector(len(self.vector))
        vector_add = [0] * len(self.vector)
        for i in range(len(self.vector)):
            vector_add[i] = self.vector[i] + second.vector[i]
        vector_result.set_vector(vector_add)
        return vector_result

    def sub_vector(self, second):
        if (len(self.vector) != len(second.vector)):
            raise DifferentSize("The vectors have different sizes")
        vector_result = Vector(len(self.vector))
        vector_sub = [0] * len(self.vector)
        for i in range(len(self.vector)):
            vector_sub[i] = self.vector[i] - second.vector[i]
        vector_result.set_vector(vector_sub)
        return vector_result

    def __sub__(self, second):
        if (len(self.vector) != len(second.vector)):
            raise DifferentSize("The matrixes have different sizes")
        vector_result = Vector(len(self.vector))
        vector_sub = [0] * len(self.vector)
        for i in range(len(self.vector)):
            vector_sub[i] = self.vector[i] - second.vector[i]
        vector_result.set_vector(vector_sub)
        return vector_result

    def write_to_file(self, name_of_file):
        res = ""
        f = open(name_of_file, 'w')
        for element in self.vector:
            res += str(element) + " "
        res += '\n'
        f.write(res)
        f.close()

    def __str__(self):
        res = ""
        for element in self.vector:
            res += str(element) + " "
        res += '\n'
        return res
