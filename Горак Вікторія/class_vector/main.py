from Vector import *
from Exception import *

f = open('error.txt', 'w')
vector1 = Vector(0)
vector2 = Vector(0)

vector1.read_vector('self.vector.txt')
vector2.read_vector('second.vector.txt')
print('First vector:')
print(vector1)
print('Second vector:')
print(vector2)
try:
    vector_add = vector1 + vector2
    vector_add.write_to_file('vector_result.txt')
    print('Addition of vectors:')
    file = open('vector_result.txt', 'r')
    print(file.read())
    file.close()
except DifferentSize as error:
    f.write(str(error))
    print(error)
try:
    vector_sub = vector1 - vector2
    vector_sub.write_to_file('vector_result2.txt')
    print('Subtraction of vectors:')
    file = open('vector_result2.txt', 'r')
    print(file.read())
    file.close()
except DifferentSize as error:
    f.write(str(error))
    print(error)
f.close()
