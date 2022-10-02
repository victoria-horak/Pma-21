from vector.Vector import Vector

first_vector_file = "sources\\vector1.txt"
second_vector_file = "sources\\vector2.txt"

print("First vector :")
first_vector = Vector(first_vector_file)
print(first_vector)

print("\nSecond vector :")
second_vector = Vector(second_vector_file)
print(second_vector)

print("\nFirst vector + Second vector:")
add_vector = first_vector + second_vector
print(add_vector)

print("\nFirst vector - Second vector:")
sub_vector = first_vector - second_vector
sub_vector.write_vector_in_file()
print(sub_vector)

print("\nFirst vector * Second vector:")
mult_vector = first_vector * second_vector
print(mult_vector)
