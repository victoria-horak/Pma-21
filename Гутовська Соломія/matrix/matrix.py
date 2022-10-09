from cgitb import text
import re
from datetime import datetime

class MatrixAddingError(Exception):
    pass

def read_matrix(path):
    lines = []
    with open(path, "r") as textFile:
        for line in textFile:
            if not line.isspace():
                lines.append(list(map(int, re.sub(' +', ' ', line).split())))
        return lines

def print_matrix(matrix):
    for row in matrix:
        print ('  '.join(map(str, row)))

def add_matrix(matrix1, matrix2):
    if (len(matrix1) != len(matrix2)) or (len(matrix1[0]) != len(matrix2[0])):
        raise MatrixAddingError("Cannot add two matrices")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def write_matrix(path, matrix):
    with open(path, 'w') as textFile:
        for row in matrix:
            textFile.write(' '.join(str(line) for line in row) + '\n')

try:
    matrix1 = read_matrix("matrix1.txt")
    print("First matrix : ")
    print_matrix(matrix1)

    matrix2 = read_matrix("matrix2.txt")
    print("\nSecond matrix : ")
    print_matrix(matrix2)
    
    resultMatrix = add_matrix(matrix1, matrix2)
    print("\nResult matrix : ")
    print_matrix(resultMatrix)

    write_matrix("resultMatrix.txt", resultMatrix)

except Exception as exc:
    file = open("logfile.txt", "a") 
    file.write("[" + str(datetime.now()) + "] Error : " + str(exc) + '\n')
    print("Error occured : " + str(exc))
