from matrix import Matrix
from error_size1 import Error_size


def matrix_to_file(line, matrix):
    file = open(matrix, "w")
    file.write(line)
    file.close()


try:
    first_matrix = []
    second_matrix = []
    first_matrix = Matrix(first_matrix)
    second_matrix = Matrix(second_matrix)
    first_matrix.read_matrix_from_file('first_matrix.txt')
    second_matrix.read_matrix_from_file('second_matrix.txt')

    print("--FIRST MATRIX--")
    print(first_matrix)
    print("--SECOND MATRIX--")
    print(second_matrix)

    adding_result = first_matrix + second_matrix
    print("--RESULT OF ADDING--")
    print(adding_result)

    subtraction_result = first_matrix - second_matrix
    print("--RESULT OF SUBTANTION--")
    print(subtraction_result)

    matrix_to_file("--RESULT OF ADDING--\n" + str(adding_result) + "\n--RESULT OF SUBTANTION--\n" + str(subtraction_result),
                   "result_matrix.txt")

except Error_size as e:
    file = open('result_matrix.txt', 'w')
    file.write(str(e))
    print(e)
    file.close()