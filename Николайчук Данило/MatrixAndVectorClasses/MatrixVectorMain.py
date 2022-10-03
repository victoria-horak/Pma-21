import differentExceptions
from MatrixClass import *
from Vector import *

fileOutput = open("outputMatrix.txt", "a")
try:
    print("First matrix:")
    matrix1 = Matrix.fillFromFileStatic("FirstMatrix.txt")
    matrix1.show()

    print("\nSecond matrix:")
    matrix2 = Matrix.fillFromFileStatic("SecondMatrix.txt")
    matrix2.show()

    print("\nMatrix of adding: ")
    matrixOfAdd = Matrix.addStatic(matrix1, matrix2)
    matrixOfAdd.show()

    print("\nSubtraction matrix:")
    subtractionMatrix = matrix2.__sub__(matrix1)
    Matrix.showStatic(subtractionMatrix)

    fileOutput.write("Add matrix:\n")
    matrixOfAdd.fillFileWithMatrix(fileOutput)
    fileOutput.write("Subtraction matrix:\n")
    Matrix.fillFileWithMatrixStatic(subtractionMatrix, fileOutput)
    fileOutput.close()
except differentExceptions.DifferentError as exc:
    fileOutput.write("Error: " + str(exc) + "\n")
    print("Error: " + str(exc))
except ValueError as exc:
    fileOutput.write("Error: " + str(exc) + "\n")
    print("Error: " + str(exc))
except IndexError as exc:
    fileOutput.write("Error: " + str(exc) + "\n")
    print("Error: " + str(exc))
fileOutput.close()

fileOutputVector = open("vectorOutput.txt", "a")
try:
    print("\nFirst vector:")
    firstVector = Vector.fillFromFileStatic("VectorFirst.txt")
    firstVector.show()

    print("\nSecond vector: ")
    secondVector = Vector.fillFromFileStatic("VectorSecond.txt")
    Vector.showStatic(secondVector)

    print("\nVector of adding:")
    vectorOfAdd = firstVector + secondVector
    vectorOfAdd.show()
    fileOutputVector.write("Vector of adding:")
    Vector.fillFileWithVectorStatic(vectorOfAdd, fileOutputVector)

    print("\nVector of subtraction:")
    vectorSub = Vector.subStatic(firstVector, secondVector)
    Vector.showStatic(vectorSub)
    fileOutputVector.write("Vector of subtraction:")
    vectorSub.fillFileWithVector(fileOutputVector)
except differentExceptions.DifferentError as exc:
    fileOutputVector.write("Error: " + str(exc))
    print("Error: " + str(exc))
except ValueError as exc:
    fileOutputVector.write("Error: " + str(exc))
    print("Error: " + str(exc))
fileOutputVector.close()
