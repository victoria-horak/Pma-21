from Matrix import Matrix
from Vector import Vector
from differSize import differSize
from differLength import differLength


#матриці
try:
    result_matrix = open('result_matrix.txt', 'w')
    print('first matrix: ')
    first = []
    firstMatrix = Matrix(first)
    firstMatrix.read_Matrix('Matrix1.txt')
    print("first matrix has been read")

    print('second matrix: ')
    second = []
    secondMatrix = Matrix(second)
    secondMatrix.read_Matrix('Matrix2.txt')
    print("second matrix has been read")

    result_add_matrix = firstMatrix + secondMatrix
    result_add_matrix.write_to_file(result_add_matrix, 'result_matrix.txt')
    print('2 matrixes has been added')

     result_sub_matrix = firstMatrix - secondMatrix
     result_sub_matrix.write_to_file(result_sub_matrix, 'result_matrix.txt')
     print('2 matrixes has been substracted')

    result_matrix.close()
except differSize as error:
    print(error)


вектори
 try:
     print('First vector:')
     first = Vector(5)
     first.read_from_file('vector1.txt')
     first.print_vectors()

     print('\nSecond vector:')
     second = Vector(5)
     second.read_from_file('vector2.txt')
     second.print_vectors()

     result_vector = open('result_vector.txt', 'w')

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

     result_vector.close()

 except differLength as error:
     print(error)
