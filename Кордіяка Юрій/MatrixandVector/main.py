from Exceptions.InvalidLengthException import InvalidLenghtException
from models.Vector import Vector
from models.Matrix import Matrix
from Exceptions.DeterminantException import DeterminantException
from Exceptions.DifferentLengtException import DifferentLengthException

file_matrix = open('information/result.txt', 'a')
file_vector = open('information/result_for_vector.txt', 'a')

try:
    matrix = Matrix('information/data.txt')
    matrix2 = Matrix('information/data1.txt')
    print("Matrix1\n" + str(matrix))
    print("Matrix2\n" + str(matrix2))
    matrix_mult = matrix * matrix2
    print('multiplication\n' + str(matrix * matrix2))
    matrix_mult.write_to_file('information/result.txt')
    matrix_div = matrix / matrix2
    matrix_div.write_to_file('information/result.txt')
    print('division\n' + str(matrix / matrix2))

    vector1 = Vector('information/for_vector.txt')
    vector2 = Vector('information/for_vector2.txt')
    vector_mult=vector1 * vector2
    file_vector.write(str(vector_mult)+'\n')
    print('multiplication\n' + str(vector1 * vector2))
    vector_sub=vector1 / vector2
    file_vector.write(str(vector_sub) + '\n')
    print('division\n' + str(vector1 / vector2))


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
except DeterminantException as e:
    print(str(e))
finally:
    file_vector.close()
    file_matrix.close()
