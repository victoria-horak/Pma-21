class differentsize(Exception):
    """When the vectors have different size"""
class vector:
    def __init__(self,n):
        self.vector =[[0]*n]
    def set_vector(self,a):
        self.vector=a
        return self.vector

    def read_vector(self, name_of_file):
        file = open(name_of_file, 'r')
        a = []
        s = file.read().replace('\n',' ')
        c=s.split()
        for i in range(len(c)):
            a.append(int(c[i])),s[i].split()
        file.close()

        self.vector=a

    def add_vector(self, second):
        if (len(self.vector)!=len(second.vector)):
            raise differentsize("The vectors have different sizes")
        for i in range (len(self.vector)):
            vector_result=vector(len(self.vector))
        vector1 = [0] * len(self.vector)
        for i in range(len(self.vector)):
                vector1[i]=self.vector[i]+second.vector[i]
        vector_result.set_vector(vector1)
        return vector_result

    def __add__(self, second):
        if (len(self.vector) != len(second.vector)):
            raise differentsize("The vectors have different sizes \n")
        vector_result = vector(len(self.vector))
        vector1 = [0] * len(self.vector)
        for i in range(len(self.vector)):
                vector1[i] = self.vector[i] + second.vector[i]
        vector_result.set_vector(vector1)
        return vector_result

    def sub_vector(self, second):
        if (len(self.vector)!= len(second.vector)):
            raise differentsize("The vectors have different sizes")
        for i in range (len(self.vector)):
            vector_result=vector(len(self.vector))
        vector1 = [0] * len(self.vector)
        for i in range(len(self.vector)):
                vector1[i]=self.vector[i]-second.vector[i]
        vector_result.set_vector(vector1)
        return vector_result


    def __sub__(self, second):
        if (len(self.vector)!= len(second.vector)):
            raise differentsize("The matrixes have different sizes")
        vector_result = vector(len(self.vector))
        vector1 = [0] * len(self.vector)
        for i in range(len(self.vector)):
                vector1[i] = self.vector[i] - second.vector[i]
        vector_result.set_vector(vector1)
        return vector_result

    def write_to_file(self, name_of_file):
        res = ""
        f= open(name_of_file, 'w')
        for element in self.vector:
            res += str(element) + " "
        res += '\n'
        f.write(res)
        f.close()
    def __str__(self):
        res=""
        for element in self.vector:
            res += str(element) + " "
        res += '\n'
        return res
f=open('error.txt', 'w')
vector1=vector(0)
vector2=vector(0)

vector1.read_vector('self.vector.txt')
vector2.read_vector('second.vector.txt')
print('First vector:')
print(vector1)
print('Second vector:')
print (vector2)
try:
    vector_add= vector1+ vector2
    vector_add.write_to_file('vector_result.txt')
    print('Addition of vectors:')
    file = open('vector_result.txt', 'r')
    print(file.read())
    file.close()
except differentsize as error:
    f.write(str(error))
    print(error)
try:
    vector_sub= vector1- vector2
    vector_sub.write_to_file('vector_result2.txt')
    print('Subtraction of vectors:')
    file = open('vector_result2.txt', 'r')
    print(file.read())
    file.close()
except differentsize as error:
    f.write(str(error))
    print(error)
file.close()