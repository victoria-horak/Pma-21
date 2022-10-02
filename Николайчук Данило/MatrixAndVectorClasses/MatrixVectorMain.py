import ExceptionsMatrix
from MatrixClass import *

try:
    print("First matrix:")
    matrix1 = Matrix.fillFromFileStatic("FirstMatrix.txt")
    matrix1.show()

    print("\nSecond matrix:")
    tempMatrix = [[1,45,3,53],[4,5,6,13],[7,8,9,6],[4,3,5,6]]
    matrix2 = Matrix(tempMatrix)
    matrix2.show()

    print("\nMatrix of adding: ")
    matrixOfAdd = Matrix.add(matrix1, matrix2)
    matrixOfAdd.show()

    print("\nSubtraction matrix:")
    subtractionMatrix = matrix2.__sub__(matrix1)
    Matrix.showStatic(subtractionMatrix)

    fileOutput = open("outputMatrix.txt", "a")
    fileOutput.write("Add matrix:\n")
    matrixOfAdd.fillFileWithMatrix(fileOutput)
    fileOutput.write("Subtraction matrix:\n")
    Matrix.fillFileWithMatrixStatic(subtractionMatrix,fileOutput)
    fileOutput.close()
except ExceptionsMatrix.NotMatrix as exc:
    print("Error: " + str(exc))
except ExceptionsMatrix.IfMatrixAreNotSameSize as exc:
    print("Error: " + str(exc))
except ExceptionsMatrix.IfLengthIsZero as exc:
    print("Error: "+str(exc))
except ValueError as exc:
    print("Error: "+str(exc))
except:
    print("Unknown error.")

import ExceptionsVector
from  Vector import *

try:
    print("\nFirst vector:")
    firstVector = Vector.fillFromFileStatic("VectorFirst.txt")
    firstVector.show()

    print("\nSecond vector:")
    secondVector = Vector([4, 8, 9, 6, 7, 8])
    Vector.showStatic(secondVector)

    fileOutput = open("vectorOutput.txt", "a")
    print("\nVector of adding:")
    vectorOfAdd = firstVector + secondVector
    vectorOfAdd.show()
    fileOutput.write("Vector of adding:")
    Vector.fillFileWithVectorStatic(vectorOfAdd, fileOutput)

    print("\nVector of subtraction:")
    vectorSub = Vector.sub(firstVector,secondVector)
    Vector.showStatic(vectorSub)
    fileOutput.write("Vector of subtraction:")
    vectorSub.fillFileWithVector(fileOutput)
    fileOutput.close()
except ExceptionsVector.NotVecto as exc:
    print("Error: "+str(exc))
except ExceptionsVector.IfLengthIsZero as exc:
    print("Error: "+str(exc))
except ExceptionsVector.IfVectorsAreNotSameSize as exc:
    print("Error: "+str(exc))
except ValueError as exc:
    print("Error: "+str(exc))
except:
    print("Unknown error.")