import re


class Matrix:
    def __init__(self, matrix=[]):
        self.matrix = []
        if not isinstance(matrix, list) or (len(matrix) > 0 and not isinstance(matrix[0], list)):
            raise Exception('Parameter is not a matrix')
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                try:
                    int(matrix[i][j])
                except ValueError:
                    print('Matrix has to contain only numbers')
                    exit(0)
        if matrix != []:
            self.matrix = matrix

    def read_matrix(self, path):
        lines = []
        currRow = []
        with open(path, "r") as textFile:
            for line in textFile:
                if not line.isspace():
                    try:
                        currRow = list(map(int, re.sub(' +', ' ', line).split()))
                        lines.append(currRow)
                    except ValueError as exception:
                        print(exception)
                        exit(0)
        self.matrix = lines

    @classmethod
    def read_matrix_static(cls, path):
        matrix = Matrix()
        matrix.read_matrix(path)
        return matrix

    def console_matrix(self):
        try:
            rowsCount = int(input('Enter amount of rows = '))
            colsCount = int(input('Enter amount of columns = '))
            if (rowsCount < 0 or colsCount < 0):
                raise ValueError(
                    "values are equal to rowsCount = " + str(rowsCount) + ", colsCount = " + str(colsCount))
        except ValueError as exception:
            print("Entered parameters cannot be less than zero! : " + str(exception))
            exit(0)
        lines = []
        for i in range(rowsCount):
            currRow = []
            for j in range(colsCount):
                valueIJ = input('matrix[' + str(i) + '][' + str(j) + '] = ')
                try:
                    number = int(valueIJ)
                    currRow.append(number)
                except ValueError:
                    print('Entered value has to be a number!')
                    exit(0)
            lines.append(currRow)
        self.matrix = lines

    @classmethod
    def console_matrix_static(cls):
        matrix = Matrix()
        matrix.console_matrix()
        return matrix

    def print_matrix(self):
        if len(self.matrix) == 0:
            raise Exception('Cannot print empty matrix')
        for row in self.matrix:
            print('  '.join(map(str, row)))

    @classmethod
    def print_matrix_static(cls, matrix):
        matrix.print_matrix()

    def add_matrix(self, anotherMatrix):
        if len(self.matrix) != len(anotherMatrix.matrix):
            raise Exception("Cannot add two matrices with different sizes of rows")
        result = []
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(anotherMatrix.matrix[i]):
                raise Exception("Cannot add two matrices with different sizes of columns")
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + anotherMatrix.matrix[i][j])
            result.append(row)
        return Matrix(result)

    @classmethod
    def add_matrix_static(cls, matrix1, matrix2):
        return matrix1.add_matrix(matrix2)

    def sub_matrix(self, anotherMatrix):
        if len(self.matrix) != len(anotherMatrix.matrix):
            raise Exception("Cannot substract two matrices with different sizes of rows")
        result = []
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(anotherMatrix.matrix[i]):
                raise Exception("Cannot substract two matrices with different sizes of columns")
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] - anotherMatrix.matrix[i][j])
            result.append(row)
        return Matrix(result)

    @classmethod
    def sub_matrix_static(cls, matrix1, matrix2):
        return matrix1.sub_matrix(matrix2)

    def write_matrix(self, path, header=''):
        if len(self.matrix) == 0:
            raise Exception('Cannot write empty matrix')
        with open(path, 'a') as textFile:
            if header != '':
                textFile.write(header + '\n')
            for row in self.matrix:
                textFile.write(' '.join(str(line) for line in row) + '\n')
            textFile.write('\n')

    @classmethod
    def write_matrix_static(cls, matrix, path, header=''):
        matrix.write_matrix(path, header)


try:
    print('First matrix : ')
    m1 = Matrix()
    m1.read_matrix('matrix1.txt')
    m1.print_matrix()

    print('\nSecond matrix :')
    m2 = Matrix.read_matrix_static('matrix2.txt')
    Matrix.print_matrix_static(m2)

    print('\nAdd matrices :')
    result = m1.add_matrix(m2)
    result.print_matrix()
    result.write_matrix('resultMatrix.txt', 'Add matrices : ')

    print('\nSubstract matrices :')
    result = Matrix.sub_matrix_static(m1, m2)
    Matrix.print_matrix_static(result)
    Matrix.write_matrix_static(result, 'resultMatrix.txt', 'Substract matrices : ')

    print('\nCreate matrix :')
    m3 = Matrix.console_matrix_static()
    Matrix.print_matrix_static(m3)
    Matrix.write_matrix_static(m3, 'resultMatrix.txt', 'Entered matrix from console : ')
except Exception as exception:
    print(exception)
