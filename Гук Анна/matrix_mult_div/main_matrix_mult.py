from Matrix_mult import Matrix
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

    mult_result = first_matrix * second_matrix
    print("--RESULT OF MULTIPLICATION--")
    print(mult_result)



    div_result = first_matrix / second_matrix
    print("--RESULT OF DIVISION--")
    print(div_result)

    matrix_to_file("--RESULT OF MULTIPLICATION--\n" + str(mult_result) + "--RESULT OF DIVISION--\n" + str(div_result),
                   "result_matrix.txt")

except Error_size as e:
    file = open('result_matrix.txt', 'w')
    file.write(str(e))
    print(e)
    file.close()