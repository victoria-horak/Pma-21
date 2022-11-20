from InvalidSize import InvalidSize


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def enter_Vector(self, file_name):
        with open(file_name, "r") as file:
            temp_vector = []
            for str in file:
                for element in str.replace(" ", "").replace("\n", ""):
                    temp_vector.append(element)
            temp_vector = [element for element in temp_vector if element]
            temp_vector = [int(element) for element in temp_vector if element]
            self.vector = temp_vector
        file.close()
        return self.vector

    @staticmethod
    def print_vector_to_file(str, filename):
        file = open(filename, "w")
        file.write(str)
        file.close()

    def __str__(self):
        return str(self.vector)

    def __add__(self, other):
        if len(self.vector) == len(other.vector):
            vector = [self.vector[iterator] + other.vector[iterator] for iterator in range(len(self.vector))]
            return Vector(vector)
        else:
            raise InvalidSize("Vectors are of different sizes.\n")

    def __sub__(self, other):
        if len(self.vector) == len(other.vector):
            vector = [self.vector[iterator] - other.vector[iterator] for iterator in range(len(self.vector))]
            return Vector(vector)
        else:
            raise InvalidSize("Vectors are of different sizes.\n")

    def __mul__(self, other):
        if len(self.vector) == len(other.vector):
            vector = [self.vector[iterator] * other.vector[iterator] for iterator in range(len(self.vector))]
            return Vector(vector)
        else:
            raise InvalidSize("Vectors are of different sizes.\n")

    def __truediv__(self, other):
        try:
            if len(self.vector) == len(other.vector):
                vector = [self.vector[iterator] / other.vector[iterator] for iterator in range(len(self.vector))]
                return Vector(vector)
            else:
                raise InvalidSize("Vectors are of different sizes.\n")
        except ZeroDivisionError:
            with open('vector3.txt', 'a+') as file:
                file.write("You cannot divide by zero.")
                print("You cannot divide by zero.")
