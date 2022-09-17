class IncorrectLength(Exception):
    """Raised when the lengths of the matrixes are not equal"""

def read_matrix(line):
    short_line = line.split(" ")
    length = 3
    matrix = []
    iterator = 0
    row = []
    for element in short_line:
        row.append(element)
        iterator += 1
        if iterator >= length:
            iterator = 0
            matrix.append(row)
            row = []

    return matrix

def str_matrix(mat):
    line = ""
    for row in mat:
        for element in row:
            line += str(element) + " "
        line += "\n"
    return line


def addMatrix(mat1, mat2):
    if (len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
        raise IncorrectLength("Incorrect length of matrix")
    result = []
    iterator1 = 0
    for mat1row in mat1:
        row = []
        iterator2 = 0
        for mat1elem in mat1row:
            row.append(int(mat1elem) + int(mat2[iterator1][iterator2]))
            iterator2 += 1
        result.append(row)
        iterator1 += 1
    return result

def matrix_into_file(line, matrix):
    file = open(matrix, "w")
    file.write(line)
    file.close()


matrix1 = read_matrix(open('matrix1.txt').read())
matrix2 = read_matrix(open('matrix2.txt').read())


try:
    matrix_into_file("Result Matrix:\n"+ str_matrix(addMatrix(matrix1,matrix2)), "matrix3.txt")

    print("First matrix:\n" + str_matrix(matrix1))
    print("Second matrix:\n" + str_matrix(matrix2))
    print("Result matrix:\n" + str_matrix(addMatrix(matrix1,matrix2)))
except IncorrectLength as e:
    print(e)
    f = open('matrix3.txt', 'a')
    f.write("\nError - Incorrect length of matrix")
    f.close()
