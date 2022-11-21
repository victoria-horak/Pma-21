from Matrix import Matrix
from Vector import Vector
from LengthError import LengthErrorException
from ErrorDivision import ErrorDivision

try:

    staticMatrix1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    staticMatrix2 = [[1, 0, 3], [0, 5, 0], [7, 0, 9]]
    staticMultMatrix = Matrix.matrixMultStut(staticMatrix1, staticMatrix2)
    staticMultMatrix.write_to_file("ResultMatrix.txt")
    staticDivMatrix = Matrix.truedivStatic(staticMatrix1, staticMatrix2)
    staticDivMatrix.write_to_file("ResultMatrix.txt")
    staticAddMatrix = Matrix.add_matrix(staticMatrix1, staticMatrix2)
    staticAddMatrix.write_to_file("ResultMatrix.txt")

    firstMatrix = Matrix("Matrix.txt")
    secondMatrix = Matrix("Matrix2.txt")
    addMatrix = firstMatrix + secondMatrix
    addMatrix.write_to_file("ResultMatrix.txt")
    multMatrix = firstMatrix * secondMatrix
    multMatrix.write_to_file("ResultMatrix.txt")
    divMatrix = firstMatrix / secondMatrix
    divMatrix.write_to_file("ResultMatrix.txt")

except Exception as e:
    print(str(e))

try:
    staticVectorfirst = [1, 2, 3, 4, 5]
    staticVectorsecond = [2, 3, 4, 5, 6]
    staticMultVector = Vector.mult_vectors(staticVectorfirst, staticVectorsecond)
    staticMultVector.write_to_file("ResultVector.txt")
    staticDivVector = Vector.division_vectors(staticVectorfirst, staticVectorsecond)
    staticDivVector.write_to_file("ResultVector.txt")
    staticAddVector = Vector.add_vectors(staticVectorfirst, staticVectorsecond)
    staticAddVector.write_to_file("ResultVector.txt")

    firstVector = Vector("Vector1.txt")
    secondVector = Vector("Vector2.txt")
    addVector = str(firstVector + secondVector)
    multVector = str(firstVector * secondVector)
    divisionVector = str(firstVector / 3)
    file = open("ResultVector.txt", "a")
    file.write(addVector + "\n\n")
    file.write(multVector + "\n\n")
    file.write(divisionVector + "\n")


except Exception as e:
    print(str(e))
