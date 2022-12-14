from Matrix import Matrix
from Vector import Vector
from differSize import *
from differLength import *
from InvalidDimensionsForMatrixMultiplication import *

try:
    result_matrix_file = open('result_matrix.txt', 'a')
    first = []
    second = []
    first_matrix = Matrix(first)
    second_matrix = Matrix(second)

    first_matrix.read_matrix('Matrix1.txt')
    second_matrix.read_matrix('Matrix2.txt')

    print("Matrix 1:")
    print(first_matrix)

    print("Matrix 2:")
    print(second_matrix)

    result_add_matrix = Matrix.add_static(first_matrix, second_matrix)
    print("Add of 2 matrices:")
    print(result_add_matrix)
    result_add_matrix.write('result_matrix.txt')

    result_sub_matrix = Matrix.sub_static(first_matrix, second_matrix)
    print("Sub of 2 matrices:")
    print(result_sub_matrix)
    result_sub_matrix.write('result_matrix.txt')

    result_mult_matrix = Matrix.mul_static(first_matrix, second_matrix)
    print("Mult of 2 matrices:")
    print(result_mult_matrix)
    result_mult_matrix.write('result_matrix.txt')

    result_div_matrix = Matrix.div_static(first_matrix, second_matrix)
    print("Division of 2 matrices:")
    print(result_div_matrix)
    result_div_matrix.write('result_matrix.txt')

except differSize as e:
    result_matrix_file = open('result_matrix.txt', 'a')
    result_matrix_file.write(str(e) + '\n')
    print(e)
except ValueError as e:
    result_matrix_file = open('result_matrix.txt', 'a')
    result_matrix_file.write(str(e) + '\n')
    result_matrix_file.write(str(e) + '\n')
    print("You input an incorrect data!")
finally:
    result_matrix_file.close()

try:
    result_vector_file = open('result_vector.txt', 'a')
    vec1 = []
    vec2 = []
    vector1 = Vector(vec1)
    vector2 = Vector(vec2)

    vector1.read_vector('vector1.txt')
    vector2.read_vector('vector2.txt')

    print("\nVector 1:")
    print(vector1)
    print("\nVector 2")
    print(vector2)

    result_vector_add = Vector.add_vectors(vector1, vector2)
    result_vector_file.write('\n')
    print("\nVectors adding:")
    print(result_vector_add)

    result_vector_sub = Vector.subtract_vectors(vector1, vector2)
    result_vector_sub.write('result_vector.txt')
    result_vector_file.write('\n')
    print("\nVectors subtraction")
    print(result_vector_sub)

    result_vector_mult = Vector.multiply_vectors(vector1, vector2)
    result_vector_mult.write('result_vector.txt')
    result_vector_file.write('\n')
    print('\nVector multiplication: ')
    print(result_vector_mult)

    result_vector_div = Vector.divide_vectors(vector1, vector2)
    result_vector_div.write('result_vector.txt')
    result_vector_file.write('\n')
    print('\nVector division: ')
    print(result_vector_div)

except differLength as e:
    result_vector_file = open('result_vector.txt', 'a')
    result_vector_file.write(str(e) + '\n')
    print(e)
except ValueError as e:
    result_vector_file = open('result_vector.txt', 'a')
    result_vector_file.write(str(e) + '\n')
    result_vector_file.write(str(e) + '\n')
    print("You input an incorrect data!")
finally:
    result_vector_file.close()
