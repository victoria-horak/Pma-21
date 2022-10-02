class Vector:

    def __init__(self, *vector_filename):
        if len(vector_filename) > 1:
            self.firstNumberX = vector_filename[0]
            self.secondNumberY = vector_filename[1]
            self.thirdNumberZ = vector_filename[2]
            return
        try:
            file = open(vector_filename[0], 'r')
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
        self.firstNumberX, self.secondNumberY, self.thirdNumberZ = values

    def get_first_number_x(self):
        return self.firstNumberX

    def get_second_number_y(self):
        return self.secondNumberY

    def get_third_number_z(self):
        return self.thirdNumberZ

    def __str__(self):
        return "(" + str(self.firstNumberX) + ", " + str(self.secondNumberY) + ", " + str(self.thirdNumberZ) + ")"

    def __add__(self, other_vector):
        if isinstance(other_vector, Vector):
            return Vector(self.firstNumberX + other_vector.get_first_number_x(),
                          self.secondNumberY + other_vector.get_second_number_y(),
                          self.thirdNumberZ + other_vector.get_third_number_z())

    def __sub__(self, other_vector):
        if isinstance(other_vector, Vector):
            return Vector(self.firstNumberX - other_vector.get_first_number_x(),
                          self.secondNumberY - other_vector.get_second_number_y(),
                          self.thirdNumberZ - other_vector.get_third_number_z())

    def __mul__(self, other_vector):
        if isinstance(other_vector, Vector):
            result = (self.firstNumberX * other_vector.get_first_number_x()) + (
                    self.secondNumberY * other_vector.get_second_number_y()) + (
                             self.thirdNumberZ * other_vector.get_third_number_z())
            return result

    def write_vector_in_file(self):
        try:
            with open("sources\\result.txt", "a") as vector_file:
                vector_file.write(str(self.firstNumberX) + ", ")
                vector_file.write(str(self.secondNumberY) + ", ")
                vector_file.write(str(self.thirdNumberZ) + "\n")
        finally:
            vector_file.close()
