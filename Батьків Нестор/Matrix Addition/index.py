import re

PATH = './Батьків Нестор/Matrix Addition/'


class DIffrentDImensions(Exception):
    """Raised when the matrix dimensions are not equal"""


def string_to_matrix(string):
    height = string.count("\n") + 1
    read_list = re.sub("\s+", " ", string).split(" ")
    length = len(read_list) / height
    matrix = []
    iterator = 0
    row = []
    for element in read_list:
        row.append(element)
        iterator += 1
        if iterator >= length:
            iterator = 0
            matrix.append(row)
            row = []
    return matrix


def matrix_addition(matrixA, matrixB):
    if (len(matrixA) != len(matrixB) or len(matrixA[0]) != len(matrixB[0])):
        raise DIffrentDImensions("Matrixes have diffrent dimensions")
    result_matrix = []
    iteratorI = 0
    for matrix1row in matrixA:
        row = []
        iteratorJ = 0
        for matrix1elem in matrix1row:
            row.append(int(matrix1elem) + int(matrixB[iteratorI][iteratorJ]))
            iteratorJ += 1
        result_matrix.append(row)
        iteratorI += 1
    return result_matrix


def matrix_to_string(matrix):
    string = ""
    for row in matrix:
        for elem in row:
            string += str(elem) + " "
        string += "\n"
    return string


def write_to_file(text, filePath):
    file = open(filePath, "w")
    file.write(text)
    file.close()


matrix1 = string_to_matrix(open(PATH+'matrix.txt').read())
matrix2 = string_to_matrix(open(PATH+'matrix2.txt').read())
try:
    write_to_file("Matrix1:\n"+matrix_to_string(matrix1) +
                  "\nMatrix2:\n"+matrix_to_string(matrix2) +
                  "\nResult Matrix:\n" +
                  matrix_to_string(matrix_addition(matrix1, matrix2)),
                  PATH+"resultMatrix.txt")
except DIffrentDImensions as e:
    print(e)
