class differentsize(Exception):
    """When the matrixes have different size"""
class matrix:
    def __init__(self,n,m):
        self.matrix =[[0*m]*n]
    def set_matrix(self,a):
        self.matrix=a
        return self.matrix

    def read_matrix(self, name_of_file):
        file = open(name_of_file, 'r')
        v = []
        s = file.read().split('\n')
        for i in range(len(s)):
            c = s[i].split()
            n = 0
            for j in range(len(c)):
                if (c[j].isdigit()):
                    n += 1
            if (n != 0):
                v.append(" ".join(c))
        file.close()

        self.matrix = [list(map(int, row.split())) for row in v]

    def add_matrix(self, second):
        if len(self.matrix)!= len(second.matrix) or len(self.matrix[0])!= len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        matrix_result=matrix(len(self.matrix),len(self.matrix[0]))
        matrix1 = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix1[i][j]=self.matrix[i][j]+second.matrix[i][j]
        matrix_result.set_matrix(matrix1)
        return matrix_result
    def __add__(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes \n")
        matrix_result = matrix(len(self.matrix), len(self.matrix[0]))
        matrix1 = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix1[i][j] = self.matrix[i][j] + second.matrix[i][j]
        matrix_result.set_matrix(matrix1)
        return matrix_result

    def sub_matrix(self, second):
        if len(self.matrix)!= len(second.matrix) or len(self.matrix[0])!= len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        matrix_result = matrix(len(self.matrix), len(self.matrix[0]))
        matrix1 = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix1[i][j]=self.matrix[i][j]-second.matrix[i][j]
        matrix_result.set_matrix(matrix1)
        return matrix_result

    def __sub__(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        matrix_result = matrix(len(self.matrix), len(self.matrix[0]))
        matrix1 = [[0] * len(self.matrix[i]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix1[i][j] = self.matrix[i][j] - second.matrix[i][j]
        matrix_result.set_matrix(matrix1)
        return matrix_result

    def write_to_file(self, name_of_file):
        res = ""
        f= open(name_of_file, 'w')
        for row in self.matrix:
            for element in row:
                res += str(element) + " "
            res += '\n'
        f.write(res)
        f.close()
    def __str__(self):
        res=""
        for row in self.matrix:
            for element in row:
                res += str(element) + " "
            res += '\n'
        return res
f=open('error.txt', 'w')
matrix1=matrix(0,0)
matrix2=matrix(0,0)

matrix1.read_matrix('self.matrix.txt')
matrix2.read_matrix('second.matrix.txt')
print('First matrix:')
print(matrix1)
print('Second matrix:')
print(matrix2)

try:
    matrix_add= matrix1+ matrix2
    matrix_add.write_to_file('matrix_result.txt')
    print('Addition of matrixes:')
    print(matrix_add)
except differentsize as error:
    f.write(str(error))
    print(error)
try:
    matrix_sub= matrix1- matrix2
    matrix_sub.write_to_file('matrix_result2.txt')
    print('Subtraction of matrixes:')
    print(matrix_sub)
except differentsize as error:
    f.write(str(error))
    print(error)
f.close()

