import re


class Vector:
    def __init__(self, vector=[]):
        self.vector = []
        if not isinstance(vector, list):
            raise Exception('Parameter is not a vector')
        for i in range(len(vector)):
            try:
                int(vector[i])
            except ValueError:
                print('Vector has to contain only numbers')
                exit(0)
        if vector != []:
            self.vector = vector

    def read_vector(self, path):
        vector = []
        with open(path, "r") as textFile:
            allLines = textFile.read()
            vector = list(map(int, re.sub(' \n+', ' ', allLines).split()))
            for i in range(len(vector)):
                try:
                    int(vector[i])
                except ValueError:
                    print('Vector has to contain only numbers')
                    exit(0)
        self.vector = vector

    @classmethod
    def read_vector_static(cls, path):
        vector = Vector()
        vector.read_vector(path)
        return vector

    def console_vector(self):
        try:
            count = int(input('Enter amount of elements in vector = '))
            if (count < 0):
                raise ValueError("value is equal to " + str(count))
        except ValueError as exception:
            print("Entered parameters cannot be less than zero! : " + str(exception))
            exit(0)
        vector = []
        for i in range(count):
            valueIJ = input('vector[' + str(i) + '] = ')
            try:
                number = int(valueIJ)
                vector.append(number)
            except ValueError:
                print('Entered value has to be a number!')
                exit(0)
        self.vector = vector

    @classmethod
    def console_vector_static(cls):
        vector = Vector()
        vector.console_vector()
        return vector

    def print_vector(self):
        if len(self.vector) == 0:
            raise Exception('Cannot print empty vector')
        print(self.vector)

    @classmethod
    def print_vector_static(cls, vector):
        vector.print_vector()

    def add_vector(self, anotherVector):
        if len(self.vector) != len(anotherVector.vector):
            raise Exception("Cannot add two vectors with different sizes")
        result = []
        for i in range(len(self.vector)):
            result.append(self.vector[i] + anotherVector.vector[i])
        return Vector(result)

    @classmethod
    def add_vector_static(cls, vector1, vector2):
        return vector1.add_vector(vector2)

    def sub_vector(self, anotherVector):
        if len(self.vector) != len(anotherVector.vector):
            raise Exception("Cannot substract two vectors with different sizes")
        result = []
        for i in range(len(self.vector)):
            result.append(self.vector[i] - anotherVector.vector[i])
        return Vector(result)

    @classmethod
    def sub_vector_static(cls, vector1, vector2):
        return vector1.sub_vector(vector2)

    def write_vector(self, path, header=''):
        if len(self.vector) == 0:
            raise Exception('Cannot write empty vector')
        with open(path, 'a') as textFile:
            if header != '':
                textFile.write(header + '\n')
            textFile.write(str(self.vector) + '\n')

    @classmethod
    def write_vector_static(cls, vector, path, header=''):
        vector.write_vector(path, header)


try:
    print('First vector : ')
    v1 = Vector()
    v1.read_vector('vector1.txt')
    v1.print_vector()
    v1.write_vector('resultVector.txt', 'First vector :')

    print('\nSecond vector : ')
    v2 = Vector.read_vector_static('vector2.txt')
    Vector.print_vector_static(v2)
    Vector.write_vector_static(v2, 'resultVector.txt', 'Second vector :')

    print('\nAdd vectors : ')
    result = Vector.add_vector(v1, v2)
    Vector.print_vector_static(result)
    Vector.write_vector_static(result, 'resultVector.txt', 'Add vectors :')

    print('\nSubstract vectors : ')
    result = Vector.sub_vector_static(v1, v2)
    Vector.print_vector_static(result)
    Vector.write_vector_static(result, 'resultVector.txt', 'Substract vectors :')

    enterVector = Vector.console_vector_static()
    Vector.print_vector_static(enterVector)
    Vector.write_vector_static(enterVector, 'resultVector.txt', 'Entered vector :')
except Exception as exception:
    print(exception)
