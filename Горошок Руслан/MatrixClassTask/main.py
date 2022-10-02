from matrix.Matrix import Matrix

file_name = "D:\\Python\\ClassMatrix\\sources\\first.txt"
file_name2 = "D:\\Python\\ClassMatrix\\sources\\second.txt"

print("First matrix :")
first_matrix = Matrix(file_name)
print(first_matrix)

print("\nSecond matrix:")
second_matrix = Matrix(file_name2)
print(second_matrix)

print("\nFirst matrix - Second matrix:")
sub_matrix = second_matrix - first_matrix
new_sub_matrix = Matrix(sub_matrix)
new_sub_matrix.write_matrix_in_file()
print(new_sub_matrix)

print("\nFirst matrix + Second matrix:")
add_matrix = first_matrix + second_matrix
new_add_matrix = Matrix(add_matrix)
new_add_matrix.write_matrix_in_file()
print(new_add_matrix)

print("\nFirst matrix * Second matrix:")
mult_matrix = first_matrix * second_matrix
mult_matrix.write_matrix_in_file()
print(mult_matrix)
