from VectorClass import Vector
from IncorrectSize import IncorrectSize

try:
    vector1 = []
    vector2 = []
    resultVector = []
    vector1 = Vector(vector1)
    vector2 = Vector(vector2)
    resultVector = Vector(resultVector)
    vector1.readVector('firstVector.txt')
    vector2.readVector('secondVector.txt')

    print("Vector 1:")
    print(vector1)
    print("Vector 2:")
    print(vector2)

    resultingAddVector = vector1 + vector2
    print("Sum of Vectors:")
    print(resultingAddVector)

    resultingSubVector = vector1 - vector2
    print("Substance of Vectors:")
    print(resultingSubVector)
    
    resultingMultVector = vector1 * vector2
    print("Mult of Vectors:")
    print(resultingMultVector)

    resultingDivVector = vector1 / vector2
    print("Div of Vectors:")
    print(resultingDivVector)

    resultVector.vector_to_file(
        "Result of Add:\n" + str(resultingAddVector) + "\nResult of Sub:\n" + str(resultingSubVector) + "\nResult of Mult:\n" + str(resultingMultVector) + "\nResult of Div:\n" + str(resultingDivVector), "result.txt")

except IncorrectSize as e:
    file = open('result.txt', 'w')
    file.write(str(e))
    print(e)
    file.close()
