from MatrixClass import Matrix
from IncorrectSize import IncorrectSize


def matrix_to_file(line, matrix):
    file = open(matrix, "w")
    file.write(line)
    file.close()


try:
    matrix1 = []
    matrix2 = []
    matrix1 = Matrix(matrix1)
    matrix2 = Matrix(matrix2)
    matrix1.readMatrix('firstMatrix.txt')
    matrix2.readMatrix('secondMatrix.txt')

    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)

    resultingAddMatrix = matrix1 + matrix2
    print("Sum of Matrices:")
    print(resultingAddMatrix)

    resultingSubMatrix = matrix1 - matrix2
    print("Substance of Matrices:")
    print(resultingSubMatrix)

    resultingMultMatrix = matrix1 * matrix2
    print("Mult of Matrices:")
    print(resultingMultMatrix)

    resultingDivMatrix = matrix1 / matrix2
    print("Div of Matrices:")
    print(resultingDivMatrix)

    matrix_to_file("Result of Add:\n" + str(resultingAddMatrix) + "\nResult of Sub:\n" + str(resultingSubMatrix) + \
                   "\nResult of Mult:\n" + str(resultingMultMatrix) + "\nResult of Division:\n" + str(
        resultingDivMatrix),
                   "resultMatrix.txt")

except IncorrectSize as e:
    file = open('resultMatrix.txt', 'w')
    file.write(str(e))
    print(e)
    file.close()
