from Matrix import Matrix
from Vector import Vector

try:
    matrixFirst = Matrix.readFromFile("matrixFirst.txt")
    print("First Matrix:", matrixFirst, sep="\n")
    matrixSecond = Matrix.readFromFile("matrixSecond.txt")
    print("Second Matrix:", matrixSecond, sep="\n")
    matrixResult = matrixFirst + matrixSecond
    print("Result Sum Matrix:", matrixResult, sep="\n")
    matrixResult.writeToFile("ResultMatrix.txt")
    matrixResult = Matrix.sub_matrix(matrixFirst, matrixSecond)
    matrixResult.writeToFile("ResultMatrix.txt")
    print("Result Sub Matrix:", matrixResult, sep="\n")
except Exception as e:
    print(str(e))
    with open("ResultMatrix.txt", "a") as file:
        file.write(str(e) + "\n")
try:
    vectorFirst = Vector.readFromFile("vectorFirst.txt")
    print("First Vector:", vectorFirst, sep="\n")
    vectorSecond = Vector.readFromFile("vectorSecond.txt")
    print("Second Vector:", vectorSecond, sep="\n")
    vectorResult = Vector.sum_vector(vectorFirst, vectorSecond)
    print("Result Sum Vector:", vectorResult, sep="\n")
    vectorResult.writeToFile("ResultVector.txt")
    vectorResult = Vector.sub_vector(vectorFirst, vectorSecond)
    print("Result Sub Vector:", vectorResult, sep="\n")
    vectorResult.writeToFile("ResultVector.txt")
except Exception as e:
    print(str(e))
    with open("ResultVector.txt", "a") as file:
        file.write(str(e) + "\n")
