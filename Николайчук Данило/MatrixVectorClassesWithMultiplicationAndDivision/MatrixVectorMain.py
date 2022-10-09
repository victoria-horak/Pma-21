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
    fileOutput.write("Add matrix:\n")
    matrixOfAdd.fillFileWithMatrix(fileOutput)

    print("\nSubtraction matrix:")
    subtractionMatrix = matrix2.__sub__(matrix1)
    Matrix.showStatic(subtractionMatrix)
    fileOutput.write("Subtraction matrix:\n")
    Matrix.fillFileWithMatrixStatic(subtractionMatrix, fileOutput)

    print("\nMultiplication matrix:")
    multiplicateMatrix = matrix1 * matrix2
    multiplicateMatrix.show()
    fileOutput.write("Multiplication matrix:\n")
    multiplicateMatrix.fillFileWithMatrix(fileOutput)

    print("\nDivision of matrix: ")
    divisionMatrix = matrix1 / matrix2
    divisionMatrix.show()
    fileOutput.write("Division of matrix:\n")
    divisionMatrix.fillFileWithMatrix(fileOutput)

    fileOutput.close()
except differentExceptions.DifferentError as exc:
    print("Error: " + str(exc))
except ValueError as exc:
    print("Error: " + str(exc))
except IndexError as exc:
    print("Error: " + str(exc))

fileOutput = open("vectorOutput.txt", "a")
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
    fileOutput.write("Vector of adding:")
    Vector.fillFileWithVectorStatic(vectorOfAdd, fileOutput)

    print("\nVector of subtraction:")
    vectorSub = Vector.subStatic(firstVector, secondVector)
    Vector.showStatic(vectorSub)
    fileOutput.write("Vector of subtraction:")
    vectorSub.fillFileWithVector(fileOutput)

    print("\nVector multiplication:")
    multiplicationVector = firstVector * secondVector
    print(f"Result of multiplication: {multiplicationVector}")
    fileOutput.write(f"Multiplication of vector: {multiplicationVector}\n")

    print("\nDivision of vector:")
    divisionVector = firstVector / secondVector
    divisionVector.show()
    fileOutput.write("Division of vector: ")
    divisionVector.fillFileWithVector(fileOutput)

    fileOutput.close()
except differentExceptions.DifferentError as exc:
    print("Error: " + str(exc))
except ValueError as exc:
    print("Error: " + str(exc))
except IndexError as exc:
    print("Error: " + str(exc))
