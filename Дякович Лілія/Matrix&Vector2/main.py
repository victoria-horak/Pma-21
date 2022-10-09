from Matrix import Matrix
from Vector import Vector
from LengthError import LengthErrorException

firstMatrix = Matrix()
secondMatrix = Matrix()
firstMatrix.read_matrix("Matrix.txt")
secondMatrix.read_matrix("Matrix2.txt")
# staticFirstMatrix = [[3, 4], [6, 7]]
# staticSecondMatrix = [[1, 2], [4, 5]]
# staticAddMatrix = Matrix.add_matrix(staticFirstMatrix, staticSecondMatrix)
# staticSubMatrix = Matrix.sub_matrix(staticFirstMatrix, staticSecondMatrix)
# staticAddMatrix.write_to_file("ResultMatrix.txt")
# staticSubMatrix.write_to_file("ResultMatrix.txt")
# print(firstMatrix, "\n")
# print(secondMatrix)
# try:
#     addedMatrix = firstMatrix + secondMatrix
#     addedMatrix.write_to_file("ResultMatrix.txt")
#     subMatrix = firstMatrix - secondMatrix
#     subMatrix.write_to_file("ResultMatrix.txt")
# except LengthErrorException as e:
#     print(str(e))
#     fileResult = open("ResultMatrix.txt", "a")
#     fileResult.write(str(e))
# try:
#     firstVector = Vector()
#     secondVector = Vector()
#     firstVector.read_vector("Vector1.txt")
#     secondVector.read_vector("Vector2.txt")
#     # standart method
#     resultAddVector = firstVector + secondVector
#     resultSubVector = firstVector - secondVector
#     resultAddVector.write_to_file("ResultVector.txt")
#     resultSubVector.write_to_file("ResultVector.txt")
#     # static
#     staticFirstVector = [1, 2, 3, 4, 5, 6]
#     staticSecondVector = [2, 3, 4, 5, 6, 7]
#     staticAddVector = Vector.add_vectors(staticFirstVector, staticSecondVector)
#     staticSubVector = Vector.sub_vectors(staticFirstVector, staticSecondVector)
#     staticSubVector.write_to_file("ResultVector.txt")
#     staticAddVector.write_to_file("ResultVector.txt")
# except Exception as e:
#     print(str(e))
#     fileResult = open("ResultVector.txt", "a")
#     fileResult.write(str(e))




matrix1= [[1,2,3],[4,5,6],[7,8,9]]
matrix2= [[1,2,3],[4,5,6],[7,8,9]]
try:
    staticMultMatrix = Matrix.matrixMultStut(matrix1,matrix2)
    staticMultMatrix.write_to_file("MultMatrix.txt")

    MultMatrix = firstMatrix * secondMatrix
    MultMatrix.write_to_file("MultMatrix.txt")

    divMatrix = firstMatrix/secondMatrix
    divMatrix.write_to_file("DivisionMatrix.txt")
except Exception as e:
    print(str(e))


try:
    firstVector = Vector()
    secondVector = Vector()
    staticVector1 = [1,2,3,4,5]
    staticVector2 = [3,4,5,6,7]
    firstVector.read_vector("Vector1.txt")
    secondVector.read_vector("Vector2.txt")
    mult = str(firstVector * secondVector)
    file = open("ResultVector.txt", "a")
    file.write(mult + "\n")
    staticMultVector = Vector.mult_vectors(staticVector1,staticVector2)
    staticMultVector.write_to_file("ResultVector.txt")

    div = firstVector/secondVector
    div.write_to_file("ResultVector.txt")
    staticDivVector = Vector.division_vectors(staticVector1,staticVector2)
    staticDivVector.write_to_file("ResultVector.txt")
except Exception as e:
    print(str(e))








