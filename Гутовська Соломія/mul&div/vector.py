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

    def print_vector(self):
        if len(self.vector) == 0:
            raise Exception('Cannot print empty vector')
        print(self.vector)

    def write_vector(self, path, header=''):
        if len(self.vector) == 0:
            raise Exception('Cannot write empty vector')
        with open(path, 'a') as textFile:
            if header != '':
                textFile.write(header + '\n')
            textFile.write(str(self.vector) + '\n')

    def mul(self, anotherVector):
        if len(self.vector) != len(anotherVector.vector):
            raise Exception("Cannot multiply two vectors with different sizes")
        result = []
        for i in range(len(self.vector)):
            result.append(self.vector[i] * anotherVector.vector[i])
        return Vector(result)

    def __mul__(self, anotherVector):
        return self.mul(anotherVector)

    def div(self, anotherVector):
        if len(self.vector) != len(anotherVector.vector):
            raise Exception("Cannot divide two vectors with different sizes")
        result = []
        for i in range(len(self.vector)):
            result.append(self.vector[i] / anotherVector.vector[i])
        return Vector(result)

    def __truediv__(self, anotherVector):
        return self.div(anotherVector)


try:
    print('First vector : ')
    v1 = Vector()
    v1.read_vector('vector1.txt')
    v1.print_vector()
    v1.write_vector('resultVector.txt', 'First vector :')

    print('\nSecond vector : ')
    v2 = Vector()
    v2.read_vector('vector2.txt')
    v2.print_vector()
    v2.write_vector('resultVector.txt', 'Second vector :')

    print('\nMultiply vectors : ')
    result = v1 * v2
    result.print_vector()
    result.write_vector('resultVector.txt', 'Multiply vectors :')

    print('\nMultiply vectors : ')
    result = v1 / v2
    result.print_vector()
    result.write_vector('resultVector.txt', 'Divide vectors :')

except Exception as exception:
    print(exception)
