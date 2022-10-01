from Matrix import Matrix
from function import read_matrix
from InvalidLengthException import InvalidLenghtException
from Vector import Vector
from DifferentLengtException import DifferentLengthException

file_matrix = open('result.txt', 'a')
file_vector = open('result_for_vector.txt', 'a')

try:
    # matrix1 = read_matrix('data.txt', 3, 3)
    # matrix3 = read_matrix('data1.txt', 3, 3)
    # matrix_static = Matrix.read_matrix_static('data.txt', 3, 3)
    # matrix_static2 = Matrix.read_matrix_static('data1.txt', 3, 3)
    # add_matrix = Matrix.add_matrix(matrix_static, matrix_static2)
    # sub_matrix = Matrix.sub_matrix_static(matrix_static, matrix_static2)
    # Matrix.write_to_file_static('result.txt', add_matrix)
    # Matrix.write_to_file_static('result.txt', sub_matrix)
    # matrix1 = Matrix()
    # matrix2 = Matrix()
    # matrix1.read_matrix('data.txt', 3, 2)
    # matrix2.read_matrix('data1.txt', 3, 2)
    # print('MATRIX 1 \n' + str(matrix1))
    # print('MATRIX 2 \n' + str(matrix2))
    # result_matrix_add = matrix1 + matrix2
    # result_matrix_add.write_to_file('result.txt')
    # print('matrix addition\n' + str(result_matrix_add))
    # result_matrix_sub = matrix1 - matrix2
    # result_matrix_sub.write_to_file('result.txt')
    # print('matrix  subtraction\n' + str(result_matrix_sub))
    # VECTOR
    # vector1=[1,3,4]
    # vector2 = [1, 3, 4]
    vector_class = Vector.read_vector_static('for_vector.txt')
    vector_class2 = Vector.read_vector_static('for_vector2.txt')
    add_vectors = Vector.add_vector_static(vector_class, vector_class2)
    sub_vector = Vector.sub_vector_static(vector_class, vector_class2)
    Vector.write_to_file_static('result_for_vector.txt', add_vectors)
    Vector.write_to_file_static('result_for_vector.txt', sub_vector)
    vector1 = Vector()
    vector2 = Vector()
    vector1.read_vector('for_vector.txt')
    vector2.read_vector('for_vector2.txt')
    print('vector 1\n' + str(vector1))
    print('vector 2\n' + str(vector2))
    result_vector_add = vector1 + vector2
    result_vector_add.write_to_file('result_for_vector.txt')
    print('vector addition\n' + str(result_vector_add))
    result_vector_sub = vector1 - vector2
    result_vector_sub.write_to_file('result_for_vector.txt')
    print('vector subtraction\n' + str(result_vector_sub))
except InvalidLenghtException as e:
    file_matrix.write(str(e) + '\n')
    print(e)
except ValueError as e:
    file_matrix.write(str(e) + '\n')
    file_vector.write(str(e) + '\n')
    print("You input incorrect data")
except DifferentLengthException as e:
    file_vector.write(str(e) + '\n')
    print(e)
except FileNotFoundError:
    print("File not found")
finally:
    file_vector.close()
    file_matrix.close()
