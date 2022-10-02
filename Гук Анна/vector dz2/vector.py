from error_size import Error


class Vector():
    def __init__(self, vector):
        self.vector = vector



    def read_vector_from_file(self, file_name):
        with open(file_name, "r") as file:
            temp_vector = []
            for line in file:
                for element in line.replace(" ", ""):
                    temp_vector.append(element)
            temp_vector = [element for element in temp_vector if element]
            temp_vector = [int(element) for element in temp_vector if element]
            self.vector = temp_vector
        file.close()
        return self.vector



    def __add__(self, other):
        if len(self.vector) == len(other.vector):
            result = [self.vector[i] + other.vector[i] for i in range(len(self.vector))]
            return Vector(result)
        else:
            raise Error("!!!FIRST VECTOR HAS DIFFERENT SIZE!!!\n")


    def __sub__(self, other):
        if len(self.vector) == len(other.vector):
            result = [self.vector[iterator] - other.vector[iterator] for iterator in range(len(self.vector))]
            return Vector(result)
        else:
            raise Error("!!!FIRST VECTOR HAS DIFFERENT SIZE!!!\n")

    def __str__(self):
        return str(self.vector)

    def write_vector_to_file(self, line, filename):
        file = open(filename, "w")
        file.write(line)
        file.close()