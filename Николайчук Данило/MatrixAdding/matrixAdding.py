# Matrix adding program
class IfMatrixAreNotSameSize(Exception):
    "Raise when size of matrix isn`t same."
    pass

class IfLengthIsZero(Exception):
    "Raise when matrix is empty."

def showMatrix(matrix):
    if len(matrix)==0:
        raise IfLengthIsZero
    for rowIterator in range(0, len(matrix)):
        print(matrix[rowIterator])

def fillingMatrixWithInfoFromFile(file):
    matrix = []
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
    if len(matrix)==0:
        raise IfLengthIsZero
    return matrix

def addingMatrix(matrixFirst, matrixSecond):
    matrixOfAdding = []
    if len(matrixFirst) != len(matrixSecond):
        raise IfMatrixAreNotSameSize
    for rowIterator in range(0, len(matrixFirst)):
        row = []
        for columnIterator in range(0, len(matrixFirst)):
            element = matrixFirst[rowIterator][columnIterator] + matrixSecond[rowIterator][columnIterator]
            row.append(element)
        matrixOfAdding.append(row)
    return matrixOfAdding

def fillingTheFileWithMatrix(matrix, file):
    if len(matrix)==0:
        raise IfLengthIsZero
    for rowIterator in range(0, len(matrix)):
        for columnIterator in range(0, len(matrix)):
            if len(matrix) - 1 == columnIterator:
                file.write(str(matrix[rowIterator][columnIterator]))
                file.write("\n")
            else:
                file.write(str(matrix[rowIterator][columnIterator]))
                file.write(",")

try:
    fileInput = open("firstAndSecondMatrix.txt")
    fileOutput = open("outputMatrix.txt", "a")

    matrixFirst = fillingMatrixWithInfoFromFile(fileInput)
    print("First matrix:")
    showMatrix(matrixFirst)

    matrixSecond = fillingMatrixWithInfoFromFile(fileInput)
    print("Second matrix:")
    showMatrix(matrixSecond)

    matrixOfAdding = addingMatrix(matrixFirst, matrixSecond)
    print("Matrix third (Adding first and second):")
    showMatrix(matrixOfAdding)

    fillingTheFileWithMatrix(matrixOfAdding, fileOutput)

    fileInput.close()
    fileOutput.close()
except IfMatrixAreNotSameSize:
    print("The program cannot add matrix of different sizes.")
    fileOutput.write("The program cannot add matrix of different sizes.\n")
except IfLengthIsZero:
    print("The matrix is empty, so the program cannot output it.")
    fileOutput.write("The matrix is empty, so the program cannot output it.\n")
except FileNotFoundError:
    print("File wasn`t open.")
except IndexError as exc:
    print("Check the contents of the file, there are not enough elements to create a matrix of the specified size.")
    fileOutput.write(str(exc)+"\n")
except ValueError as exc:
    print("Incorrect data in file (the program cannot convert characters into numbers).")
    fileOutput.write(str(exc)+"\n")
except:
    print("Error.")