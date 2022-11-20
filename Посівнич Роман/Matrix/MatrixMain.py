class InvalidMatrix(Exception):
    pass


def enter_matrix(file_name):
    matrix = []
    file = open(file_name)
    read_from_file = file.read()
    file.close()
    split_matrix = read_from_file.split("\n")
    for row_iterator in range(0, split_matrix.__len__()):
        row_element = split_matrix[row_iterator]
        if row_element.strip() == '':
            continue
        column_element = row_element.split(" ")
        row = []
        for column_iterator in range(0, column_element.__len__()):
            element = column_element[column_iterator]
            if element == '':
                continue
            row.append(int(element))
        matrix.append(row)
    return matrix


def print_matrix_to_console(file_name):
    for iterator in range(len(file_name)):
        print(str(file_name[iterator]))


def print_matrix_to_file(matrix, file_name):
    file = open(file_name, 'a')
    for iterator in matrix:
        file.write(str(iterator) + '\n')


def addition_matrix(matrix1, matrix2, file_name):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise InvalidMatrix
    else:
        result = []
        for iterator in range(len(matrix1)):
            row = []
            for jterator in range(len(matrix1[0])):
                row.append(0)
            result.append(row)
    for iterator in range(len(matrix1)):
        for jterator in range(len(matrix1[0])):
            result[iterator][jterator] = matrix1[iterator][jterator] + matrix2[iterator][jterator]
    return result


try:
    print("Matrix1:")
    matrix1 = enter_matrix('matrix1.txt')
    print_matrix_to_console(matrix1)

    print("Matrix2:")
    matrix2 = enter_matrix('matrix2.txt')
    print_matrix_to_console(matrix2)

    print("Matrix3:")
    matrix3 = addition_matrix(matrix1, matrix2, 'matrix3.txt')
    print_matrix_to_console(matrix3)
    print_matrix_to_file(matrix3, 'matrix3.txt')


except InvalidMatrix as error:
    print("Matrices are of different sizes.")
