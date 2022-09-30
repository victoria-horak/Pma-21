from Matrix import *
from Vector import *
from DifferentSizesVectors import *

file_matrix = open('Dataresult.txt', 'a')
file_vector = open('VectorResult.txt', 'a')

try:
    #################################
    """Matrixes"""
    #################################
    empty_matrix1 = []
    empty_matrix2 = []
    matrix1 = Matrix(empty_matrix1)
    matrix2 = Matrix(empty_matrix2)
    matrix1.read_matrix('Data1.txt')
    matrix2.read_matrix('Data2.txt')

    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)

    result_matrix_add = matrix1 + matrix2
    print("Add of matrix:")
    print(result_matrix_add)

    result_matrix_add.write_to_file('Dataresult.txt')

    result_matrix_sub = matrix1 - matrix2
    print("Sub of matrix:")
    print(result_matrix_sub)

    result_matrix_sub.write_to_file('Dataresult.txt')

except DifferentSizes as e:
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

    result_vector_add = vector1 + vector2

    result_vector_add.write_to_file('VectorResult.txt')
    file_vector.write('\n')

    print("\nVectors add:")
    print(result_vector_add)

    result_vector_sub = vector1 - vector2
    result_vector_sub.write_to_file('VectorResult.txt')

    print("\nVectors sub")
    print(result_vector_sub)
except DifferentSizesVectors as e:
    file_vector.write(str(e)+'\n')
    print(e)

file_vector.close()
