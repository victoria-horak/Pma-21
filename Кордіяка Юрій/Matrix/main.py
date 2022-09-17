class InvalidLenght(Exception):
    pass


def read_matrix_str(file_name):
    with open(file_name, "r") as file:
        matrix = []
        for line in file:
            matrix.append(line.strip().split(','))
    file.close()
    return matrix


def convert_matrix_int(matrix):
    for iterator in range(0, len(matrix)):
        for jiterator in range(0, len(matrix[0])):
            matrix[iterator][jiterator] = int(matrix[iterator][jiterator])
    return matrix


def add_matrix(file_name, matrix1, matrix2):
    file = open(file_name, 'a')
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    else:
        file.write(str(InvalidLenght('the lengths of the matrices do not match')) + '\n')
        raise InvalidLenght('the lengths of the matrices do not match')
    file.close()
    return result


def matrix_to_file(matrix, file_name):
    for i in matrix:
        file_name.write(str(i) + '\n')
    file_name.write('\n')


file = open('result.txt', 'a')
try:
    matrix1 = read_matrix_str('data.txt')
    matrix2 = read_matrix_str('data1.txt')

    convert_matrix_int(matrix1)
    convert_matrix_int(matrix2)

    result = add_matrix('result.txt', matrix1, matrix2)

    matrix_to_file(result, file)
    for i in result:
        print(i)
except InvalidLenght as e:
    print(e)
