from vector_mult import Vector
from error_size_vec import Error

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

    mult_result = first_vector * second_vector
    print("--VECTORS MULTIPLICATION--")
    print(mult_result)

    div_result = first_vector / second_vector
    print("--VECTORS DIVISION--")
    print(div_result)

    result_vector.write_vector_to_file(
        "--VECTORS MULTIPLICATION--\n" + str(mult_result) + "\n--VECTORS DIVISION--\n" + str(div_result), "result_vector.txt")

except Error as e:
    file = open('result_vector.txt', 'w')
    file.write(str(e) + '\n')
    print(e)
    file.close()