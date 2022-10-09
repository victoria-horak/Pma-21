from Matrix import *
from Vector import *
from DifferentSizesMatrix import *
from DifferentSizesVectors import *

file_matrix = open('MatrixResult.txt', 'a')
file_vector = open('VectorResult.txt', 'a')
#################################
"""Matrixes"""
#################################
empty_matrix1 = []
empty_matrix2 = []
matrix1 = Matrix(empty_matrix1)
matrix2 = Matrix(empty_matrix2)
matrix1.read_matrix('Matrix1.txt')
matrix2.read_matrix('Matrix2.txt')

try:
    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)

    result_matrix_mult = matrix1 * matrix2
    print("Mult of matrix:")
    print(result_matrix_mult)

    result_matrix_mult.write_to_file('MatrixResult.txt')

except DifferentSizesMatrix as e:
    file_matrix.write(str(e) + '\n')
    print(e)

try:

    result_matrix_div = matrix1 / matrix2
    print("Div of matrix:")
    print(result_matrix_div)

    result_matrix_div.write_to_file('MatrixResult.txt')

except DifferentSizesMatrix as e:
    file_matrix.write(str(e) + '\n')
    print(e)

file_matrix.close()

try:
    ####################################
    """Vectors"""
    ####################################
    empty_vector1 = []
    empty_vector2 = []
    vector1 = Vector(empty_vector1)
    vector2 = Vector(empty_vector2)

    vector1.read_vector('Vector1.txt')
    vector2.read_vector('Vector2.txt')

    print("\nVector 1:")
    print(vector1)
    print("\nVector 2")
    print(vector2)

    result_vector_mult = vector1 * vector2

    result_vector_mult.write_to_file('VectorResult.txt')
    file_vector.write('\n')

    print("\nVectors mult:")
    print(result_vector_mult)

    result_vector_div = vector1 / vector2
    result_vector_div.write_to_file('VectorResult.txt')

    print("\nVectors div")
    print(result_vector_div)
except DifferentSizesVectors as e:
    file_vector.write(str(e)+'\n')
    print(e)

file_vector.close()
