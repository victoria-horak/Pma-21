from Excpetions import *


def outputMatrixFromFile(fileName):
    resultMatrix = []
    with open(fileName) as file:
        try:
            for line in file:
                if not line.isspace():
                    line = line.split(",")
                    row = []
                    for columnIterator in range(0, len(line)):
                        element = int(line[columnIterator])
                        row.append(element)
                    resultMatrix.append(row)
        except ValueError:
            print("wrong element type")
            resultMatrix.clear()
    return resultMatrix


def outputMatrixToFile(matrix, fileName):
    try:
        with open(fileName, "w") as file:
            if matrix == []:
                raise Empty
            for i in range(0, len(matrix)):
                file.write(str(matrix[i]) + " ")
                file.write('\n')
    except Empty:
        print("vector is empty")


def outputMatrix(matrix):
    for rowIterator in range(0, len(matrix)):
        print(matrix[rowIterator])


def additionOfMatrixes(firstMatrix, secondMatrix):
    resultMatrix = []
    try:
        if (len(firstMatrix) != len(secondMatrix)):
            raise DifferentLength
        length = len(firstMatrix)
        for rowIterator in range(0, length):
            row = []
            for columnIterator in range(0, length):
                element = firstMatrix[rowIterator][columnIterator] + secondMatrix[rowIterator][columnIterator]
                row.append(element)
            resultMatrix.append(row)
    except DifferentLength:
        print("matrixes have different length")
    return resultMatrix


file = "matrix1.txt"
firstMatrix = outputMatrixFromFile(file)
print("first matrix:")
outputMatrix(firstMatrix)

file = "matrix2.txt"
secondMatrix = outputMatrixFromFile(file)
print("second matrix:")
outputMatrix(secondMatrix)

resultFile = "result.txt"
resultMatrix = additionOfMatrixes(firstMatrix, secondMatrix)
print("result matrix:")
outputMatrix(resultMatrix)
outputMatrixToFile(resultMatrix, resultFile)
