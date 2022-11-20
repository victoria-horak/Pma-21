from ClassVector import Vector
from InvalidSize import InvalidSize

try:
    vector1 = []
    vector1 = Vector(vector1)
    vector1.enter_Vector('vector1.txt')
    print("Vector 1:")
    print(vector1)

    vector2 = []
    vector2 = Vector(vector2)
    vector2.enter_Vector('vector2.txt')
    print("Vector 2:")
    print(vector2)

    vector3 = []
    vector3 = Vector(vector3)

    print("Addition:")
    print(vector1 + vector2)

    print("Subtraction:")
    print(vector1 - vector2)

    print("Multiplication:")
    print(vector1 * vector2)

    print("Division:")
    print(vector1 / vector2)

    vector3.print_vector_to_file("\nAddition:\n" + str(vector1 + vector2) +
                                 "\nSubtraction:\n" + str(vector1 - vector2) +
                                 "\nMultiplication:\n" + str(vector1 * vector2) +
                                 "\nDivision:\n" + str(vector1 / vector2), "vector3.txt")

except InvalidSize as e:
    file = open('vector3.txt', 'w')
    file.write(str(e))
    print(e)
    file.close()