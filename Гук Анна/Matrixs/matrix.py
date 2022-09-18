class AnotherSize(Exception):
    '!!!Different size of matrixes!!!'
    pass


def addition(first_matrix, second_matrix, file):
    if(len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0])):
        file = open(file, 'a')
        file.write('!First matrix has another size than second matrix!'+'\n')
        raise (Exception('!First matrix has another size than second matrix!'))

    else:
        result_matrix=[]
        for i in range(len(first_matrix)):
            row = []
            for j in range(len(first_matrix[0])):
                row.append(0)
            result_matrix.append(row)
    for i in range(len(first_matrix)):
        result_matrix[i][j]=first_matrix[i][j]+second_matrix[i][j]
    return result_matrix


def read_from_file(file):
    with open(file, 'r') as f:
        matrix = [[int(num) for num in matrix_str.split(' ')]for matrix_str in f]
    return matrix


def result(matrix, file):
    file=open(file, 'a')
    for iterator in matrix:
        file.write(str(iterator)+'\n')

try:
    first_matrix=read_from_file('first_matrix.txt')
    second_matrix=read_from_file('second_matrix.txt')
    add_matrix=addition(first_matrix, second_matrix, 'result_matrix.txt')
    result(add_matrix, 'result_matrix.txt')
except AnotherSize as exception:
    print(exception)



