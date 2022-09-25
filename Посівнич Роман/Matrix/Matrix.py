class InvalidMatrix(Exception):
    pass


def enter_matrix(file_name):
    with open(file_name, 'r') as file:
        matrix = [[int(element) for element in matrix_str.split(' ')] for matrix_str in file]
    return matrix

def file_print(matrix, file_name):
    file = open(file_name, 'a')
    for iterator in matrix:
        file.write(str(iterator) + '\n')

def addition(matrix1, matrix2, file_name):
    if (len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0])):
        file = open(file_name, 'a')
        file.write(str(InvalidMatrix("Invalid Matrix")) + '\n')
        raise InvalidMatrix("Invalid Matrix")
    else:
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(0)
            result.append(row)
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

try:
    matrix1 = enter_matrix('matrix1.txt')

    matrix2 = enter_matrix('matrix2.txt')

    matrix3 = addition(matrix1, matrix2, 'matrix3.txt')

    file_print(matrix3, 'matrix3.txt')

except InvalidMatrix as e:
    print(e)