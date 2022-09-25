from Matrix import *
from Vector import *
from DifferentSizesVectors import *

file_matrix = open('Dataresult.txt', 'a')
file_vector = open('VectorResult.txt', 'a')

try:
    #################################
    """Matrixes"""
    #################################
    matrix1 = Matrix()
    matrix2 = Matrix()
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


    ####################################
    """Vectors"""
    ####################################

    vector1 = Vector()
    vector2 = Vector()

    vector1.read_vector('Vector1.txt')
    vector2.read_vector('Vector2.txt')

    print("Vector 1:")
    print(vector1)
    print("Vector 2")
    print(vector2)

    result_vector_add = vector1 + vector2

    result_vector_add.write_to_file('VectorResult.txt')
    file_vector.write('\n')

    print("Vectors add:")
    print(result_vector_add)

    result_vector_sub = vector1 - vector2
    result_vector_sub.write_to_file('VectorResult.txt')

    print("Vectors sub")
    print(result_vector_sub)


except DifferentSizes as e:
    file_matrix.write(str(e) + '\n')
    print(e)
except DifferentSizesVectors as e:
    file_vector.write(str(e)+'\n')
    print(e)
