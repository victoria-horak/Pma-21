from Matrix import Matrix
from lengthNotMatchExeption import LengthNotMatchExeption
from Vector import Vector

try:
    matrixFirst = Matrix("matrixFirst.txt")
    print("First Matrix:", matrixFirst, sep="\n")
    matrixSecond = Matrix("matrixSecond.txt")
    print("Second Matrix:", matrixSecond, sep="\n")
    matrixResult = matrixFirst + matrixSecond
    print("Result Sum Matrix:", matrixResult, sep="\n")
    matrixResult.writeToFile("ResultMatrix.txt")
    matrixResult = matrixFirst - matrixSecond
    print("Result Subtraction Matrix:", matrixResult, sep="\n")
    matrixResult.writeToFile("ResultMatrix.txt")
    matrixResult = matrixFirst / matrixSecond
    print("Result Div Matrix:", matrixResult, sep="\n")
    matrixResult.writeToFile("ResultMatrix.txt")
    matrixResult = matrixFirst * matrixSecond
    print("Result Mul Matrix:", matrixResult, sep="\n")
    matrixResult.writeToFile("ResultMatrix.txt")
except LengthNotMatchExeption as e:
    print(str(e))
    with open("ResultMatrix.txt", "a") as file:
        file.write(str(e) + "\n")

try:
    vectorFirst = Vector("vectorFirst.txt")
    print("First Vector:", vectorFirst, sep="\n")
    vectorSecond = Vector("vectorSecond.txt")
    print("Second Vector:", vectorSecond, sep="\n")
    vectorResult = vectorFirst + vectorSecond
    vectorResult.writeToFile("ResultVector.txt")
    print("Result Sum Vector:", vectorResult, sep="\n")
    vectorResult = vectorFirst - vectorSecond
    vectorResult.writeToFile("ResultVector.txt")
    print("Result Subtraction Vector:", vectorResult, sep="\n")
    vectorResult = vectorFirst * vectorSecond
    vectorResult.writeToFile("ResultVector.txt")
    print("Result Mul Vector:", vectorResult, sep="\n")
    vectorResult = vectorFirst / vectorSecond
    vectorResult.writeToFile("ResultVector.txt")
    print("Result div Vector:", vectorResult, sep="\n")
except LengthNotMatchExeption as e:
    print(str(e))
    with open("ResultVector.txt", "a") as file:
        file.write(str(e) + "\n")
