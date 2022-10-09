class NotMatchMatrixSize(Exception):
    pass


def sum_matrix(matrix1, matrix2):
    resultOfmatrix = []
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise NotMatchMatrixSize("Matrix length not match")
    else:
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                temp = matrix1[i][j] + matrix2[i][j]
                row.append(temp)
            resultOfmatrix.append(row)
    return resultOfmatrix


matrix1 = []
matrix2 = []
file_first = open("data1.txt")
file_second = open("data2.txt")
for row in file_first.readlines():
    matrix1.append([int(x) for x in row.split(",")])
print("FIRST MATRIX")
for iterator in range(len(matrix1)):
    print(matrix1[iterator])
for row in file_second.readlines():
    matrix2.append([int(x) for x in row.split(",")])
print("SECOND MATRIX")
file_second = open("data2.txt")
for iterator in range(len(matrix2)):
    print(matrix2[iterator])
file_result = open("result.txt", "w")
try:
    resultOfmatrix = sum_matrix(matrix1, matrix2)
    print("RESULT MATRIX")
    for iterator in resultOfmatrix:
        print(str(iterator))
        file_result.write(str(iterator) + '\n')
except NotMatchMatrixSize as error:
    print(error)
    file_result.write(str(error))
    file_result.close()
