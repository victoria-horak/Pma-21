import numpy as np

class invalidLength(Exception):
    """Length does not match"""

def matrix_summary(matrix1, matrix2):
    matrix_res = []
    if len(matrix1) != len(matrix2):
        raise invalidLength
    else:
         matrix_res = np.add(matrix1,matrix2)
    return matrix_res

matrix1 = []
fileMat1 = open("matrix1.txt")
for row in fileMat1.readlines():
    matrix1.append([int(x) for x in row.split(",")])
print("first matrix: ")
for i in range(len(matrix1)):
    print(matrix1[i])
matrix2 = []
fileMat2 = open("matrix2.txt")
for row in fileMat2.readlines():
    matrix2.append([int(x) for x in row.split(",")])
print("second matrix: ")
for i in range(len(matrix2)):
    print(matrix2[i])
file_res = open("result.txt", "a")

try:
    matrix_res = matrix_summary(matrix1, matrix2)
    print("Result is:", "\n", matrix_res)
    file_res.write(str(matrix_res))
    file_res.write(str("\n"))

except invalidLength as error:
    print("Error:"+str(error))
    file_res.write(str(error))
