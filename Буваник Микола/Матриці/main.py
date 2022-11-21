from LengthNotMatchException import LengthNotMatchException


def sum_matrix(matrix_first, matrix_second):
    matrix_result = []
    if len(matrix_first) != len(matrix_second) or len(matrix_first[0]) != len(matrix_second[0]):
        raise LengthNotMatchException("Matrix length not match")
    for i in range(len(matrix_first)):
        row = []
        for j in range(len(matrix_first[0])):
            temp = matrix_first[i][j] + matrix_second[i][j]
            row.append(temp)
        matrix_result.append(row)
    return matrix_result


file_result = open("result.txt", "w")
try:
    matrix_first = []
    file_first = open("data1.txt")
    for row in file_first.readlines():
        list = [x for x in row.strip().split(",")]
        list = [int(x) for x in list if x]
        matrix_first.append(list)
    matrix_first = [x for x in matrix_first if x]
    print("FIRST MATRIX\n")
    for iterator in range(len(matrix_first)):
        print(matrix_first[iterator])
    matrix_second = []
    file_second = open("data2.txt")
    for row in file_second.readlines():
        matrix_second.append([int(x) for x in row.split(",")])
    print("SECOND MATRIX\n")
    for iterator in range(len(matrix_second)):
        print(matrix_second[iterator])
    matrix_result = sum_matrix(matrix_first, matrix_second)
    print("RESULT MATRIX")
    for iterator in matrix_result:
        print(str(iterator))
        file_result.write(str(iterator) + '\n')
except Exception as error:
    print("Error:" + str(error))
    file_result.write(str(error) + "\n")
