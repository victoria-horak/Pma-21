class differentsize(Exception):
    """When the matrixes have different size"""

class matrix:
    def __init__(self, row, column):
        self.matrix = [[0 * column] * row]

    def set_matrix(self, matrix_first):
        self.matrix = matrix_first
        return self.matrix

    def read_matrix(self, name_of_file):
        file = open(name_of_file, 'r')
        v = []
        read_text = file.read().split('\n')
        for i in range(len(read_text)):
            rows = read_text[i].split()
            n = 0
            for j in range(len(rows)):
                if (rows[j].isdigit()):
                    n += 1
            if (n != 0):
                v.append(" ".join(rows))
        file.close()

        self.matrix = [list(map(int, row.split())) for row in v]

    def mult_matrix(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        matrix_result = matrix(len(self.matrix), len(self.matrix[0]))
        matrix_mult = [[0] * len(second.matrix[0]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                for k in range(len(second.matrix[0])):
                    matrix_mult[i][j] += self.matrix[i][k] * second.matrix[k][j]
        matrix_result.set_matrix(matrix_mult)
        return matrix_result

    def __mul__(self, second):
        if len(self.matrix) != len(second.matrix) or len(self.matrix[0]) != len(second.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        matrix_result = matrix(len(self.matrix), len(self.matrix[0]))
        matrix_mult = [[0] * len(second.matrix[0]) for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                for k in range(len(second.matrix[0])):
                    matrix_mult[i][j] += self.matrix[i][k] * second.matrix[k][j]
        matrix_result.set_matrix(matrix_mult)
        return matrix_result

    def transposeMatrix(self):
        return map(list, zip(*self.matrix))

    def getMatrixMinor(self, i, j):
        return [row[:j] + row[j + 1:] for row in (self.matrix[:i] + self.matrix[i + 1:])]

    def getMatrixDeternminant(self):

        if len(self.matrix) == 2:
           return self.matrix[0][0]*self.matrix[1][1]-self.matrix[0][1]*self.matrix[1][0]
        determinant = 0
        for i in range(len(self.matrix)):
            minor = matrix(len(self.matrix), len(self.matrix))
            minor.set_matrix(self.getMatrixMinor(0, i))
            determinant += ((-1)**i) * self.matrix[0][i] * minor.getMatrixDeternminant()
        return determinant

    def getMatrixInverse(self):
        determinant = self.getMatrixDeternminant()
        if len(self.matrix) != len(self.matrix[0]):
            raise differentsize("The matrixes have different sizes")
        if len(self.matrix) == 2:
            if len(self.matrix) == 2:
                matrix_inv = matrix(2, 2)
                matrix1 = [[0 for i in range(2)] for j in range(2)]
                matrix1[0][0] = self.matrix[1][1] / determinant
                matrix1[0][1] = self.matrix[0][1] / determinant
                matrix1[1][0] = self.matrix[1][0] / determinant
                matrix1[1][1] = self.matrix[1][1] / determinant
                matrix_inv.set_matrix(matrix1)
                return matrix_inv
            
        cofactors = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                minor=matrix(len(self.matrix),len(self.matrix))
                minor.set_matrix( self.getMatrixMinor( i, j))
                cofactors[i][j] = (((-1)**(i + j)) *(minor.getMatrixDeternminant()))
        matrix_result = matrix(len(self.matrix), len(self.matrix[0]))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                cofactors[i][j] = cofactors[i][j] / determinant
        matrix_result.set_matrix(cofactors)
        matrix_result.transposeMatrix()
        return matrix_result

    def __truediv__(self,second):
        return self.mult_matrix(second.getMatrixInverse())

    def write_to_file(self, name_of_file):
        res = ""
        f = open(name_of_file, 'w')
        for row in self.matrix:
            for element in row:
                res += str(element) + " "
            res += '\n'
        f.write(res)
        f.close()

    def __str__(self):
        res = ""
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
    matrix_mul= matrix1* matrix2
    matrix_mul.write_to_file('matrix_result.txt')
    print('Multiplication of matrixes:')
    print(matrix_mul)
except differentsize as error:
    f.write(str(error))
    print(error)
try:
    matrix= matrix1 / matrix2
    matrix.write_to_file('matrix_result2.txt')
    print('Division of matrixes:')
    print(matrix)
except differentsize as error:
    f.write(str(error))
    print(error)
f.close()


