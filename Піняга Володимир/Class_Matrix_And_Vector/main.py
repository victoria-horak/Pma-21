from Matrix import Matrix
from Vector import Vector




try:

    result_matrix_file = open('result_matrix.txt', 'a')
    first = []
    second = []
    first_matrix = Matrix(first)
    second_matrix = Matrix(second)

    first_matrix.read_matrix('Matrix1.txt')
    second_matrix.read_matrix('Matrix2.txt')

    print("Matrix 1:")
    print(first_matrix)

    print("Matrix 2:")
    print(second_matrix)

    result_add_matrix = first_matrix + second_matrix
    print("Add of matrix:")
    print(result_add_matrix)
    result_add_matrix.write('result_matrix.txt')

    result_sub_matrix = first_matrix - second_matrix
    print("Sub of matrix:")
    print(result_sub_matrix)
    result_sub_matrix.write('result_matrix.txt')

except differSize as e:
    file_matrix.write(str(e) + '\n')
    print(e)

result_matrix_file.close()

try:

    result_vector_file = open('result_vector.txt', 'a')
    vec1 = []
    vec2 = []
    vector1 = Vector(vec1)
    vector2 = Vector(vec2)

    vector1.read_vector('vector1.txt')
    vector2.read_vector('vector2.txt')

    print("\nVector 1:")
    print(vector1)
    print("\nVector 2")
    print(vector2)

    result_vector_add = vector1 + vector2

    result_vector_add.write('result_vector.txt')
    result_vector_file.write('\n')

    print("\nVectors adding:")
    print(result_vector_add)

    result_vector_sub = vector1 - vector2
    result_vector_sub.write('result_vector.txt')

    print("\nVectors substraction")
    print(result_vector_sub)
except differLength as e:
    result_vector_file.write(str(e)+'\n')
    print(e)

result_vector_file.close()
