class Vector2:
    def __init__(self, vector_filename):
        if isinstance(vector_filename, list):
            self.__vector = vector_filename
        else:
            self.__vector = self.__read_vector(vector_filename)

    @staticmethod
    def __read_vector(vector_filename):
        global file
        try:
            file = open(vector_filename, 'r')
            file_lines = file.read().split("\n")
        finally:
            file.close()
        values = []
        for line_index in range(0, len(file_lines)):
            file_line = file_lines[line_index]
            if file_line == '':
                continue
            line_elements = file_line.split(" ")
            for element_index in range(0, len(line_elements)):
                line_element = line_elements[element_index]
                if line_element == '':
                    continue
                number = float(line_element)
                values.append(number)
        return values

    @property
    def vector(self):
        return self.__vector

    def __str__(self):
        return self.__vector.__str__()

    def __add__(self, other_vector):
        if isinstance(other_vector, Vector2):
            if len(self.__vector) != len(other_vector.vector):
                with open("sources\\result.txt", "a+") as vector_file:
                    vector_file.write("We cannot add this vector")
                return Vector2([])
            result = []
            for iterator in range(len(self.__vector)):
                result.append(self.__vector[iterator] + other_vector.vector[iterator])
            return Vector2(result)
        else:
            with open("sources\\result.txt", "a+") as vector_file:
                vector_file.write("We cannot add this vector")

    def __sub__(self, other_vector):
        if isinstance(other_vector, Vector2):
            if len(self.__vector) != len(other_vector.vector):
                with open("sources\\result.txt", "a+") as vector_file:
                    vector_file.write("We cannot sub this vector")
                    return Vector2([])
            result = []
            for iterator in range(len(self.__vector)):
                result.append(self.__vector[iterator] - other_vector.vector[iterator])
            return Vector2(result)
        else:
            with open("sources\\result.txt", "a+") as vector_file:
                vector_file.write("We cannot sub this vector")

    def __mul__(self, other_vector):
        if isinstance(other_vector, Vector2):
            if len(self.__vector) != len(other_vector.vector):
                with open("sources\\result.txt", "a+") as vector_file:
                    vector_file.write("We cannot mult this vector")
                    return Vector2([])
            result = []
            for iterator in range(len(self.__vector)):
                result.append(self.__vector[iterator] * other_vector.vector[iterator])
            return Vector2(result)
        else:
            with open("sources\\result.txt", "a+") as vector_file:
                vector_file.write("We cannot mult this vector")

    def __truediv__(self, other_vector):
        if isinstance(other_vector, Vector2):
            if len(self.__vector) != len(other_vector.vector):
                with open("sources\\result.txt", "a+") as vector_file:
                    vector_file.write("We cannot division this vector")
            result = []
            for iterator in range(len(self.__vector)):
                try:
                    result.append(self.__vector[iterator] / other_vector.vector[iterator])
                except ZeroDivisionError:
                    with open("sources\\result.txt", "a+") as vector_file:
                        vector_file.write("\nWe cannot division by zero\n")
                    return Vector2([])
            return Vector2(result)
        else:
            with open("sources\\result.txt", "a+") as vector_file:
                vector_file.write("We cannot division vector")

    def write_vector_in_file(self):
        try:
            with open("sources\\result.txt", "a+") as vector_file:
                for iterator in self.vector:
                    vector_file.write(str(iterator))
                    vector_file.write(" ")
                vector_file.write("\n")
        finally:
            vector_file.close()
