from Matrix import Matrix
from InvalidLengthException import InvalidLenghtException
from Vector import Vector
from DifferentLengtException import  DifferentLengthException

file_matrix = open('result.txt', 'a')
file_vector = open('result_for_vector.txt', 'a')

try:

    matrix1 = Matrix()
    matrix2 = Matrix()
    matrix1.read_matrix('data.txt')
    matrix2.read_matrix('data1.txt')
    print('MATRIX 1 \n' + str(matrix1))
    print('MATRIX 2 \n' + str(matrix2))
    result_matrix_add = matrix1 + matrix2
    result_matrix_add.write_to_file('result.txt')
    print('matrix addition\n' + str(result_matrix_add))
    result_matrix_sub = matrix1 - matrix2
    result_matrix_sub.write_to_file('result.txt')
    print('matrix  subtraction\n' + str(result_matrix_sub))
    vector1 = Vector()
    vector2 = Vector()
    vector1.read_matrix('for_vector.txt')
    print('vector 1\n' + str(vector1))
    vector2.read_matrix('for_vector2.txt')
    print('vector 2\n' + str(vector2))
    result_vector_add = vector1 + vector2
    result_vector_add.write_to_file('result_for_vector.txt')
    file_vector.write('\n')
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
    file_vector.write(str(e)+'\n')
    print(e)

except FileNotFoundError:
    print("File not found")
file_vector.close()
file_matrix.close()