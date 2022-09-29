class WrongSize(Exception):
    """The size of two matrices is not the same"""


def add_two_matrices(mtrx1, mtrx2):
    if len(mtrx1) != len(mtrx2) or len(mtrx1[0]) != len(mtrx2[0]):
        raise WrongSize("The matrices have different size")
    result = [[0] * len(mtrx1[i]) for i in range(len(mtrx1))]
    for i in range(len(mtrx1)):
        for j in range(len(mtrx1[i])):
            result[i][j] = mtrx1[i][j] + mtrx2[i][j]
    return result


print("Matrix 1:")
file = open('matrix1.txt', 'r')
print(file.read())
file.close()
print("\nMatrix 2:")
file = open('matrix2.txt', 'r')
print(file.read())
file.close()

with open('matrix1.txt') as f:
    matrix1 = [list(map(int, row.split())) for row in f.readlines()]
with open('matrix2.txt') as f:
    matrix2 = [list(map(int, row.split())) for row in f.readlines()]

print("\nResult:")
file = open("resulting_matrix.txt", 'w')
try:
    resulting_matrix = add_two_matrices(matrix1, matrix2)
    for row in range(len(resulting_matrix)):
        file.write(str(resulting_matrix[row]) + '\n')
        print(resulting_matrix[row])
except WrongSize as error:
    print(error)
    file.write(str(error))

file.close()
