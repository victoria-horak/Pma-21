from Vector import *
from Matrix import *

firstVector = Vector.staticReadFromFile("vector1.txt")
secondVector = Vector()
secondVector.readFromFile("vector2.txt")
resultVector = Vector()
resultVector = firstVector / secondVector
resultVector = Vector.staticDivision(firstVector, secondVector)
Vector.staticPrintToFile("vectorData.txt", resultVector)
mul = firstVector * secondVector
print("firstMatrix * secondMatrix" + " = " + str(mul))

firstMatrix = Matrix()
firstMatrix.readFromFile("matrix1.txt")
secondMatrix = Matrix()
secondMatrix.readFromFile("matrix2.txt")
resultMatrix = secondMatrix / firstMatrix
resultMatrix.printToFile("resultMatrix.txt")
