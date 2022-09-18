class DifferentDimensions(Exception):
    pass
#reads a matrix from file
def GetMatrix(fileName):
    with open(fileName, 'r') as file:
        matrix = [[int(value) for value in currentLine.split(' ')] for currentLine in file]
    return matrix
#adds two matrices, exception if dimensions are different
def AddMatrices(matrix1, matrix2):
    file = open('answer.txt', 'w')
    if (len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0])):
        file.write(str(DifferentDimensions("Matrices are of different sizes")) + '\n')
        file.close()
        raise DifferentDimensions("Matrices are of different sizes")
    else:
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(0)
            result.append(row)
    for rowIterator in range(len(matrix1)):
        for columnIterator in range(len(matrix1[0])):
            result[rowIterator][columnIterator] = matrix1[rowIterator][columnIterator] + matrix2[rowIterator][columnIterator]
    for rowIterator in range(result.__len__()):
        currentLine = ''
        for columnIterator in range(result[rowIterator].__len__()):
            currentLine += str(result[rowIterator][columnIterator]) + ' '
        file.write(currentLine + '\n')
    file.close()
try:
    matrix1 = GetMatrix('Matrix1.txt')
    matrix2 = GetMatrix('Matrix2.txt')
    AddMatrices(matrix1, matrix2)  
except DifferentDimensions as error:
    print(error)
    file = open('answer.txt')
    file.write(error)
    file.close()
