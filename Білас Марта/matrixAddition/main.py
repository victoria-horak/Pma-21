class DifferentLength(Exception):
    "matrixes have different lengthes"
    pass

def outputMatrixFromFile(matrix):
    length = int(file.read(1))
    lineOfMatrix = file.readline()
    for rowIterator in range(0, length):
        lineOfMatrix = file.readline()
        line = lineOfMatrix.split(",")
        row = []
        for columnIterator in range(0, length):
            element = int(line[columnIterator])
            row.append(element)
        matrix.append(row)


def outputMatrixToFile(matrix):
    for rowIterator in range(0, len(matrix)):
         for columnIterator in range(0, len(matrix)):
             resultFile.write(str(matrix[rowIterator][columnIterator]) + " ")
         resultFile.write('\n')
    resultFile.close()

def outputMatrix(matrix):
    for rowIterator in range (0, len(matrix)):
        print(matrix[rowIterator])

def additionOfMatrixes(firstMatrix, secondMatrix,resultMatrix):
    length = len(firstMatrix)
    for rowIterator in range(0, length):
        row = []
        for columnIterator in range(0, length):
            element = firstMatrix[rowIterator][columnIterator] + secondMatrix[rowIterator][columnIterator]
            row.append(element)
        resultMatrix.append(row)

file = open("data.txt")
firstMatrix = []
outputMatrixFromFile(firstMatrix)
print("first matrix:")
outputMatrix(firstMatrix)

secondMatrix = []
outputMatrixFromFile(secondMatrix)
print("second matrix:")
outputMatrix(secondMatrix)
file.close()

resultFile = open("result.txt", "a")
try:
    if(len(firstMatrix) != len(secondMatrix)):
        raise DifferentLength
    resultMatrix = []
    additionOfMatrixes(firstMatrix, secondMatrix, resultMatrix)
    print("result matrix:")
    outputMatrix(resultMatrix)
    outputMatrixToFile(resultMatrix)
except DifferentLength:
    print("matrixes have different length")
    resultFile.write("matrixes have different length"+"\n")
    resultFile.close()



