def read_from_file(file):
    with open(file, 'r') as f:
        matrix = [[int(num) for num in matrix_str.split()] for matrix_str in f]
    return matrix


def output_result(matrix, file):
    file = open(file, 'a')
    for i in matrix:
        file.write(str(i) + '\n')


def add_two_matrices(matrix_one, matrix_two):
    resulting_matrix = []
    for i in range(len(matrix_one)):
        row = []
        for j in range(len(matrix_one[0])):
            row.append(0)
        resulting_matrix.append(row)

    for i in range(len(matrix_one)):
        for j in range(len(matrix_one[0])):
            resulting_matrix[i][j] = matrix_one[i][j] + matrix_two[i][j]
    return resulting_matrix


matrix1 = read_from_file('matrix1.txt')
matrix2 = read_from_file('matrix2.txt')
add_matrices = add_two_matrices(matrix1, matrix2)
output_result(add_matrices, 'result.txt')
