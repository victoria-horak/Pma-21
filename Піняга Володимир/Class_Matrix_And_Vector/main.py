from Matrix import Matrix
from Vector import Vector
from Matrix import differSize
result_matrix = open('result_matrix.txt', 'w')
result_vector = open('result_vector.txt', 'w')

#матриці
try:
    print('first matrix: ')
    firstMatrix = Matrix(3,3)
    firstMatrix.Enter_Matrix('Matrix1.txt')
    print("first matrix has been read")

    print('second matrix: ')
    secondMatrix = Matrix(3,3)
    secondMatrix.Enter_Matrix('Matrix2.txt')
    print("second matrix has been read")

    result_add_matrix = Matrix(3,3)
    result_add_matrix.Add_2matrix(firstMatrix, secondMatrix, 'result_matrix.txt')
    result_add_matrix.write(result_add_matrix, 'result_matrix.txt')
    print('2 matrixes has been added')

    result_sub_matrix = Matrix(3,3)
    result_sub_matrix.Substract_2matrix(firstMatrix, secondMatrix, 'result_matrix.txt')
    result_sub_matrix.write(result_sub_matrix, 'result_matrix.txt')
    print('2 matrixes has been added')

except differSize as error:
    print(error)


#вектори
try:
    print('First vector:')
    first = Vector(5)
    first.read_from_file('vector1.txt')
    first.print_vectors()

    print('\nSecond vector:')
    second = Vector(5)
    second.read_from_file('vector2.txt')
    second.print_vectors()

    # print('\nAdding: first vector + second vector: ')
    result_add_vector = Vector(5)
    result_add_vector = first.add_2_vectors(second)
    # result_add_vector.print_vectors()
    result_add_vector.write_result()
    print('\n2 vectors have been added')

    # print('\nSubstraction: first vector - second vector: ')
    result_sub_vector = Vector(5)
    result_sub_vector = first.substract_2_vectors(second)
    # result_sub_vector.print_vectors()
    result_sub_vector.write_result()
    print('2 vectors have been substracted')
except differLength as error:
    print(error)