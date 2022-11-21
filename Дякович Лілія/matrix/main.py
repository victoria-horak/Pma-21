from LengthError import LengthError
def addMatrix(matrix1, matrix2):
    matrixResult = []
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise LengthError("matrices have different lengths")
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
    list = [x for x in row.strip().split(",")]
    list = [int(x) for x in list if x]
    matrix1.append(list)
matrix1 = [x for x in matrix1 if x]


for i in range(len(matrix1)):
    print(matrix1[i])
file1.close()
print("\n")

for row in file2.readlines():
    list = [x for x in row.strip().split(",")]
    list = [int(x) for x in list if x]
    matrix2.append(list)
matrix2 = [x for x in matrix2 if x]

for i in range(len(matrix2)):
    print(matrix2[i])
file2.close()


try:
    file3 = open("result-matrix.txt", "a")
    matrixResult = addMatrix(matrix1, matrix2)
    for iterator in matrixResult:
        file3.write(str(iterator)+"\n")
    file3.write("\n")
    file3.close()
    

except LengthError as e:
    file3 = open("result-matrix.txt", "a")
    print(str(e))
    file3.write(str(e))
    file3.close()
