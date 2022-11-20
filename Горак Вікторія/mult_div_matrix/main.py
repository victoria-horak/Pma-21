from Matrix import *
from Exception import *


f = open('error.txt', 'w')
matrix1 = Matrix(0, 0)
matrix2 = Matrix(0, 0)

matrix1.read_matrix('self.matrix.txt')
matrix2.read_matrix('second.matrix.txt')
print('First matrix:')
print(matrix1)
print('Second matrix:')
print(matrix2)

try:
    matrix_mul = matrix1 * matrix2
    matrix_mul.write_to_file('matrix_result.txt')
    print('Multiplication of matrixes:')
    print(matrix_mul)
except DifferentSize as error:
    f.write(str(error))
    print(error)
try:
    matrix = matrix1 / matrix2
    matrix.write_to_file('matrix_result2.txt')
    print('Division of matrixes:')
    print(matrix)
except DifferentSize as error:
    f.write(str(error))
    print(error)

f.close()
