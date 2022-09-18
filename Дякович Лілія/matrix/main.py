class lengthError(Exception):
    pass


def addMatrix(matrix1, matrix2):
    matrixResult = []
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise lengthError("matrices have different lengths")
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        matrixResult.append(row)
    return matrixResult


matrix1 = []
matrix2 = []
file1 = open("matrix-1.txt")
file2 = open("matrix-2.txt")

for row in file1.readlines():
    matrix1.append([int(x) for x in row.split(",")])
for i in range(len(matrix1)):
    print(matrix1[i])

print("\n")

for row in file2.readlines():
    matrix2.append([int(x) for x in row.split(",")])
for i in range(len(matrix2)):
    print(matrix2[i])

try:
    file3 = open("result-matrix.txt", "a")
    matrixResult = addMatrix(matrix1, matrix2)
    for iterator in matrixResult:
        file3.write(str(iterator)+"\n")
    file3.write("\n")

except lengthError as e:
    print(str(e))
    file3.write(str(e))