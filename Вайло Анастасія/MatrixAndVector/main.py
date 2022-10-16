from Matrix import Matrix
from Vector import Vector

result = open("result.txt")
result_vector = open('result_vector.txt')

try:
    first_matrix = Matrix("FirstMatrix.txt")
    second_matrix = Matrix("SecondMatrix.txt")
    result_matrix = first_matrix * second_matrix
    Matrix.write_to_file(result_matrix, "result.txt")
except Exception as ex:
    result.write(str(ex))    

try:
    first_vector = Vector('FirstVector.txt')
    second_vector = Vector('SecondVector.txt')
    result_vec = first_vector - second_vector
    Vector.write_to_file(result_vec, 'result_vector.txt')
except Exception as e:
    result_vector.write(str(e))