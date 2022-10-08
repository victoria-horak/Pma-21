from Matrix import Matrix
from Vector import Vector
from DifferentDimensionsException import DifferentDimensionsException
from DifferentLengthsException import DifferentLengthsException
from NonValidDimensionsForMultiplicationException import NonValidDimensionsForMultiplicationException

resultForMatrices = open('resultForMatrices.txt', 'a')
resultForVectors = open('resultForVectors.txt', 'a')

try:
    firstMatrix = Matrix()
    secondMatrix = Matrix()

    firstMatrix.readFromFile("Matrix1.txt")
    secondMatrix.readFromFile("Matrix2.txt")

    resultMatrix = firstMatrix.divideMatrices_NonStatic(secondMatrix)
    resultMatrix.writeToFile("resultForMatrices.txt")
    print('Two matrices are multiplied')
except DifferentDimensionsException as e:
    resultForMatrices.write(str(e))
except NonValidDimensionsForMultiplicationException as e:
    resultForMatrices.write(str(e))

try:
    firstVector = Vector()
    secondVector = Vector()

    firstVector.readFromFile('Vector1.txt') 
    secondVector.readFromFile('Vector2.txt')
    resultVector = Vector.divideVectors_Static(firstVector, secondVector)
    resultOfMultiplication = Vector.multiplyVector_Static(firstVector, secondVector)
    resultVector.writeToFile('resultForVectors.txt')

    resultForVectors.write('result of multiplication: ' + str(resultOfMultiplication))
    resultForVectors.close()
except DifferentLengthsException as e:
    resultForVectors.write(str(e))
