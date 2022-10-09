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
sub_matrix.write_matrix_in_file()
print(sub_matrix)

print("\nFirst matrix + Second matrix:")
add_matrix = first_matrix + second_matrix
add_matrix.write_matrix_in_file()
print(add_matrix)

print("\nFirst matrix * Second matrix:")
mult_matrix = first_matrix * second_matrix
mult_matrix.write_matrix_in_file()
print(mult_matrix)

print("\nFirst matrix / Second matrix:")
div_matrix = second_matrix / first_matrix
div_matrix.write_matrix_in_file()
print(div_matrix)

