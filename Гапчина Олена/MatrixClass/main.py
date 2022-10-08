from Matrix import Matrix, WrongSize

print("Matrix A:")
first_matrix = Matrix(Matrix.read_from_file("first_matrix.txt"))
first_matrix.print()

print("\nMatrix B:")
second_matrix = Matrix(Matrix.read_from_file("second_matrix.txt"))
second_matrix.print()

try:
    print("\nA + B:")
    matrix_sum = Matrix(first_matrix.add(second_matrix))
    matrix_sum.print()
    matrix_sum.write_to_file("matrix_sum.txt")

    print("\nA - B:")
    matrix_subtraction = Matrix(first_matrix.subtract(second_matrix))
    matrix_subtraction.print()
    matrix_subtraction.write_to_file("matrix_subtraction.txt")

    print("\nA * B:")
    matrix_multiplication = Matrix(first_matrix.multiply(second_matrix))
    matrix_multiplication.print()
    matrix_multiplication.write_to_file("matrix_multiplication.txt")

    print("\nA / B:")
    matrix_division = Matrix.divide_matrices(first_matrix, second_matrix)
    matrix_division.print()
    matrix_division.write_to_file("matrix_division.txt")
except WrongSize as error:
    print(error)
    file = open("errors.txt", 'w')
    file.write(str(error))
    file.close()

print("\nB^(-1):")
transposed_second_matrix = Matrix(second_matrix.transpose())
transposed_second_matrix.print()
