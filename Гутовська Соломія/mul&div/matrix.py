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

    def print_matrix(self):
        if len(self.matrix) == 0:
            raise Exception('Cannot print empty matrix')
        for row in self.matrix:
            print('  '.join(map(str, row)))

    def write_matrix(self, path, header=''):
        if len(self.matrix) == 0:
            raise Exception('Cannot write empty matrix')
        with open(path, 'a') as textFile:
            if header != '':
                textFile.write(header + '\n')
            for row in self.matrix:
                textFile.write(' '.join(str(line) for line in row) + '\n')
            textFile.write('\n')

    def mul(self, anotherMatrix):
        if len(self.matrix[0]) != len(anotherMatrix.matrix):
            raise Exception(
                'The number of columns of the first matrix is not equal to the number of rows of the second matrix')
        result = []
        for i in range(len(self.matrix)):
            currRow = []
            for j in range(len(anotherMatrix.matrix[0])):
                currRow.append(0)
                for k in range(len(self.matrix[0])):
                    currRow[-1] += self.matrix[i][k] * anotherMatrix.matrix[k][j]
            result.append(currRow)
        return Matrix(result)

    def __mul__(self, anotherMatrix):
        return self.mul(anotherMatrix)

    def div(self, other):
        return self.mul(other.reverseMatrix())

    def __truediv__(self, other):
        return self.div(other)

    def getMatrixMinor(self, i, j):
        return Matrix([row[:j] + row[j + 1:] for row in (self.matrix[:i] + self.matrix[i + 1:])])

    def getMatrixDeterminant(self):
        if len(self.matrix) == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        if len(self.matrix) == 3:
            return self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2] + \
                self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0] + \
                self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1] - \
                self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0] - \
                self.matrix[0][1] * self.matrix[1][0] * self.matrix[2][2] - \
                self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]
        return 0

    def transposeMatrix(self):
        return Matrix([[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))])

    def reverseMatrix(self):
        determinant = self.getMatrixDeterminant()
        if determinant == 0:
            raise Exception("Determinant of second matrix cannot be equal to 0")
        if len(self.matrix) == 2 and len(self.matrix[0]) == 2:
            return Matrix([[self.matrix[1][1] / determinant, -self.matrix[0][1] / determinant],
                           [-self.matrix[1][0] / determinant, self.matrix[0][0] / determinant]])
        elif len(self.matrix) == 3 and len(self.matrix[0]) == 3:
            aMatrix = []
            for i in range(len(self.matrix)):
                currRow = []
                for j in range(len(self.matrix[0])):
                    currRow.append((-1)**(i + j) * self.getMatrixMinor(i, j).getMatrixDeterminant())
                aMatrix.append(currRow)
            TransposedAMatrix = Matrix(aMatrix).transposeMatrix()
            for i in range(len(TransposedAMatrix.matrix)):
                currRow = []
                for j in range(len(TransposedAMatrix.matrix[0])):
                    TransposedAMatrix.matrix[i][j] = TransposedAMatrix.matrix[i][j] / determinant
            return TransposedAMatrix
        return Matrix([])

try:
    print('First matrix : ')
    m1 = Matrix()
    m1.read_matrix('matrix1.txt')
    m1.print_matrix()

    print('\nSecond matrix :')
    m2 = Matrix()
    m2.read_matrix('matrix2.txt')
    m2.print_matrix()

    print('\nMultiply matrices :')
    result = m1 * m2
    result.print_matrix()
    result.write_matrix('resultMatrix.txt', 'Multiply matrices : ')

    print('\nDivide matrices :')
    result = m1 / m2
    result.print_matrix()
    result.write_matrix('resultMatrix.txt', 'Divide matrices : ')

except Exception as exception:
    print(exception)
