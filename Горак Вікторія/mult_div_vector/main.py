class differentsize(Exception):
    """When the vectors have different size"""

class vector:
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

    def mult_vector(self, second):
        if (len(self.vector) != len(second.vector)):
            raise differentsize("The vectors have different sizes")
        for i in range(len(self.vector)):
            vector_result = vector(len(self.vector))
        vector_mult = [0] * len(self.vector)
        for i in range(len(self.vector)):
            vector_mult[i] = self.vector[i] * second.vector[i]
        vector_result.set_vector(vector_mult)
        return vector_result

    def __mul__(self, second):
        if (len(self.vector) != len(second.vector)):
            raise differentsize("The vectors have different sizes")
        for i in range(len(self.vector)):
            vector_result = vector(len(self.vector))
        vector_mult = [0] * len(self.vector)
        for i in range(len(self.vector)):
            vector_mult[i] = self.vector[i] * second.vector[i]
        vector_result.set_vector(vector_mult)
        return vector_result

    def __truediv__(self, second):
        if (len(self.vector) != len(second.vector)):
            raise differentsize("The vectors have different sizes")
        vector_result = vector(len(self.vector))
        vector_div = [0] * len(self.vector)
        for i in range(len(self.vector)):
            vector_div[i] = self.vector[i] / second.vector[i]
        vector_result.set_vector(vector_div)
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


f = open('error.txt', 'w')
vector1 = vector(0)
vector2 = vector(0)

vector1.read_vector('self.vector.txt')
vector2.read_vector('second.vector.txt')
print('First vector:')
print(vector1)
print('Second vector:')
print(vector2)
try:
    vector_mult = vector1 * vector2
    vector_mult.write_to_file('vector_result.txt')
    print('Multiplication of vectors:')
    file = open('vector_result.txt', 'r')
    print(file.read())
    file.close()
except differentsize as error:
    f.write(str(error))
    print(error)
try:
    vector_div = vector1 / vector2
    vector_div.write_to_file('vector_result2.txt')
    print('Division of vectors:')
    file = open('vector_result2.txt', 'r')
    print(file.read())
    file.close()
except differentsize as error:
    f.write(str(error))
    print(error)
file.close()