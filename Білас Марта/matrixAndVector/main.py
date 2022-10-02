from Vector import *
from Matrix import *

vector1 = Vector()
vector1.readFromFile("vector1.txt")
vector2 = Vector()
vector2.readFromFile("vector2.txt")
resultVector = Vector()
resultVector = vector1 + vector2
resultVector.printToFile("vectorData.txt")

matrix1 = Matrix()
matrix1.readFromFile("matrix1.txt")
matrix2 = Matrix()
matrix2.readFromFile("matrix2.txt")
resultMatrix = Matrix()
resultMatrix = matrix1 + matrix2
resultMatrix.printToFile("resultMatrix")
