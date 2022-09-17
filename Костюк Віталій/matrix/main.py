

class DiffrentSizes(Exception):
    pass


def input_matrix(file_name):
    with open(file_name, 'r') as file:
        matrix = [[int(element) for element in matrix_str.split(' ')] for matrix_str in file]
    return matrix


def add_matrix(matrix1, matrix2, file_name):
    if (len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0])):
        file = open(file_name, 'a')
        file.write(str(DiffrentSizes("Matrixes have different sizes")) + '\n')
        raise DiffrentSizes("Matrixes have different sizes")
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


def print_to_file(matrix, file_name):
    file = open(file_name, 'a')
    for iterator in matrix:
        file.write(str(iterator) + '\n')


try:
    matrix1 = input_matrix('text1.txt')
    matrix2 = input_matrix('text2.txt')
    result_matrix = add_matrix(matrix1, matrix2, 'text.txt')
    print_to_file(result_matrix, 'text.txt')
except DiffrentSizes as e:
    print(e)