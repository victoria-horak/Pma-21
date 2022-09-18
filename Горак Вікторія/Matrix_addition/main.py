print("matrix1:")
file = open('matrix1.txt', 'r')
print(file.read())
file.close()
print("matrix2:")
file = open('matrix2.txt', 'r')
print(file.read())
file.close()
print("matrix_result:")
file = open('error.txt', 'w')

class differentsize(Exception):
     """when the size of one matrix is not equal to the other"""
matrix1=[]
matrix2=[]
with open('matrix1.txt') as f:
    matrix1= [list(map(int, row.split())) for row in f.readlines()]
with open('matrix2.txt') as f:
    matrix2 = [list(map(int, row.split())) for row in f.readlines()]

def add_matrix(matrix1,matrix2, name_of_file):
    if len(matrix1)!= len(matrix2) or len(matrix1[0])!= len(matrix2[0]):
     raise differentsize ("The matrixes have different sizes")
    file = open(name_of_file, 'w')
    matrix_result=[[0]*len(matrix1[i]) for i in range (len(matrix1))]
    res=""
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix_result[i][j]=matrix1[i][j]+matrix2[i][j]
    for row in matrix_result:
        for element in row:
            res+= str(element) + " "
        res+='\n'
    print(matrix_result)
    file.write(res)
    file.close()
try:
    add_matrix= add_matrix(matrix1, matrix2, 'matrix_result.txt')
except differentsize as error:
    print(error)
    file.write(error)
    file.close()