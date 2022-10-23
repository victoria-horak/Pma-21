from Vector import Vector, DifferentSize

first_vector = Vector(Vector.read_from_file("first_vector.txt"))
print("Vector A: ", end=' ')
first_vector.print()

second_vector = Vector(Vector.read_from_file("second_vector.txt"))
print("\nVector B: ", end=' ')
second_vector.print()

try:
    vector_sum = Vector(first_vector.add(second_vector))
    vector_sum.write_to_file("vector_sum.txt")

    vector_subtraction = Vector(first_vector.subtract(second_vector))
    vector_subtraction.write_to_file("vector_subtraction.txt")

    vector_multiplication = Vector(first_vector.multiply(second_vector))
    vector_multiplication.write_to_file("vector_multiplication.txt")

    vector_division = Vector(first_vector.divide(second_vector))
    vector_division.write_to_file("vector_division.txt")
    
except DifferentSize as error:
    print(error)
