from Vector import Vector

first_vector = Vector(Vector.read_from_file("first_vector.txt"))
second_vector = Vector(Vector.read_from_file("second_vector.txt"))

vector_sum = Vector(first_vector.add(second_vector))
vector_sum.write_to_file("vector_sum.txt")

vector_subtraction = Vector(first_vector - second_vector)
vector_subtraction.write_to_file("vector_subtraction.txt")
