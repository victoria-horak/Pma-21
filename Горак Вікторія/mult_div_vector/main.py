from Vector import *
from Exception import*


f = open('error.txt', 'w')
vector1 = Vector(0)
vector2 = Vector(0)

vector1.read_vector('self.vector.txt')
vector2.read_vector('second.vector.txt')
print('First vector:')
print(vector1)
print('Second vector:')
print(vector2)

print('Scalar of vectors:')
print(vector1 * vector2)
print('Multiplication of vectors:')
file = open('vector_result.txt', 'r')
print(file.read())
file.close()

try:
    vector_div = vector1 / vector2
    vector_div.write_to_file('vector_result2.txt')
    print('Division of vectors:')
    file = open('vector_result2.txt', 'r')
    print(file.read())
    file.close()
except DifferentSize as error:
    f.write(str(error))
    print(error)
f.close()
