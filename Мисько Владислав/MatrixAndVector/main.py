from Matrix import Matrix
from Vector import Vector
from DifferentDimensionsException import DifferentDimensionsException
from DifferentLengthsException import DifferentLengthsException

resultForMatrices = open('resultForMatrices.txt', 'w')
resultForVectors = open('resultForVectors.txt', 'w')

try:
    firstMatrix = Matrix()
    secondMatrix = Matrix()

    firstMatrix.ReadFromFile("Matrix1.txt")
    secondMatrix.ReadFromFile("Matrix2.txt")

    resultMatrix = firstMatrix + secondMatrix
    resultMatrix.WriteToFile("resultForMatrices.txt")
    print('Two matrices are added')
except DifferentDimensionsException as e:
    resultForVectors.write(str(e))

try:
    firstVector = Vector()
    secondVector = Vector()

    firstVector.ReadFromFile('Vector1.txt') 
    secondVector.ReadFromFile('Vector2.txt')
    
    resultVector = firstVector + secondVector
    resultVector.WriteToFile('resultForVectors.txt')
    print('Two vectors are added')
except DifferentLengthsException as e:
    resultForMatrices.write(str(e))