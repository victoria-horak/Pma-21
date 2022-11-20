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
    matrix_add = matrix1 + matrix2
    matrix_add.write_to_file('matrix_result.txt')
    print('Addition of matrixes:')
    print(matrix_add)
except differentsize as error:
    f.write(str(error))
    print(error)
try:
    matrix_sub = matrix1 - matrix2
    matrix_sub.write_to_file('matrix_result2.txt')
    print('Subtraction of matrixes:')
    print(matrix_sub)
except differentsize as error:
    f.write(str(error))
    print(error)
f.close()
