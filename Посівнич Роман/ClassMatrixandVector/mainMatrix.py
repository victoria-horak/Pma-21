from ClassMatrix import *
from InvalidSize import *

try:
    file_matrix = open('matrix3.txt', 'a')

    matrix1 = []
    matrix1 = Matrix(matrix1)
    matrix1.enter_Matrix('matrix1.txt')
    print("Matrix 1:")
    print(matrix1)

    matrix2 = []
    matrix2 = Matrix(matrix2)
    matrix2.enter_Matrix('matrix2.txt')
    print("Matrix 2:")
    print(matrix2)

    matrix_addition = matrix1 + matrix2
    print("Addition:")
    print(matrix_addition)
    matrix_addition.print_matrix_to_file('matrix3.txt')

    matrix_subtraction = matrix1 - matrix2
    print("Subtraction:")
    print(matrix_subtraction)
    matrix_subtraction.print_matrix_to_file('matrix3.txt')

    matrix_multiplication = matrix1 * matrix2
    print("Multiplication:")
    print(matrix_multiplication)
    matrix_multiplication.print_matrix_to_file('matrix3.txt')


except InvalidSize as e:
    file_matrix.write(str(e) + '\n')
    print(e)

