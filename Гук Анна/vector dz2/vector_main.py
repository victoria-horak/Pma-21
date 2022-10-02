from vector import Vector
from error_size import Error

try:
    first_vector = []
    second_vector = []
    result_vector = []
    first_vector = Vector(first_vector)
    second_vector = Vector(second_vector)
    result_vector = Vector(result_vector)
    first_vector.read_vector_from_file('first_vector.txt')
    second_vector.read_vector_from_file('second_vector.txt')

    print("FIRST VECTOR ")
    print(first_vector)
    print("SECOND VECTOR")
    print(second_vector)

    adding_result = first_vector + second_vector
    print("Adding of Vectors:")
    print(adding_result)

    subtraction_result = first_vector - second_vector
    print("Subtraction of Vectors:")
    print(subtraction_result)

    result_vector.write_vector_to_file(
        "Result of Add:\n" + str(adding_result) + "\nResult of Sub:\n" + str(subtraction_result), "result_vector.txt")

except Error as e:
    file = open('result_vector.txt', 'w')
    file.write(str(e) + '\n')
    print(e)
    file.close()