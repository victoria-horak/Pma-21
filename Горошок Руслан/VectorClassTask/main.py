from vector.Vector2 import Vector2

first_vector_file = "sources\\vector1.txt"
second_vector_file = "sources\\vector2.txt"

print("first_vector :")
first_vector = Vector2(first_vector_file)
print(first_vector)

print("second_vector :")
second_vector = Vector2(second_vector_file)
print(second_vector)

print("Add two vector :")
add_vector = first_vector + second_vector
add_vector.write_vector_in_file()
print(add_vector)

print("sub two vector :")
sub_vector = first_vector - second_vector
sub_vector.write_vector_in_file()
print(sub_vector)

print("mult two vector :")
multiply_vector = first_vector * second_vector
multiply_vector.write_vector_in_file()
print(multiply_vector)

print("div two vector :")
division_vector = first_vector / second_vector
division_vector.write_vector_in_file()
print(division_vector)
