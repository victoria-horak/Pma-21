class lengthNotMatch(Exception):
    pass

def sum_matrix(matrix_first, matrix_second):
    matrix_result = []
    if len(matrix_first) != len(matrix_second) or len(matrix_first[0]) != len(matrix_second[0]):
        raise lengthNotMatch("Matrix length not match")
    for i in range(len(matrix_first)):
        row = []
        for j in range(len(matrix_first[0])):
            temp = matrix_first[i][j] + matrix_second[i][j]
            row.append(temp)
        matrix_result.append(row)
    return matrix_result


matrix_first = []
file_first = open("data1.txt")
for row in file_first.readlines():
    matrix_first.append([int(x) for x in row.split(",")])
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
file_result = open("result.txt", "a")
try:
    matrix_result = sum_matrix(matrix_first, matrix_second)
    print("RESULT MATRIX")
    for iterator in matrix_result:
        print(str(iterator))
        file_result.write(str(iterator) + '\n')
except lengthNotMatch as eror:
    print("Eror:"+str(eror))
    file_result.write(str(eror) + "\n")
