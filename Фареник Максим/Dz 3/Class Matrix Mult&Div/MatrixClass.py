from IncorrectSize import IncorrectSize


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def get_matrix(self):
        return self.matrix

    def get_row(self, iterator):
        return self.matrix[iterator]

    def get_element(self, kterator, jterator):
        return self.matrix[kterator][jterator]

    def readMatrix(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                temp_matrix = [element for element in line.replace(" ", "").replace("\n", "")]
                temp_matrix = [int(element) for element in temp_matrix]
                self.matrix.append(temp_matrix)
            self.matrix = [element for element in self.matrix if element]
        file.close()
        return self.matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix1 = [[self.matrix[iterator][jterator] + other.matrix[iterator][jterator] for jterator in
                        range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(matrix1)
        else:
            raise IncorrectSize("Error!!! Matrices have different sizes!!!\n")

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix1 = [[self.matrix[iterator][jterator] - other.matrix[iterator][jterator] for jterator in
                        range(len(self.matrix[0]))] for iterator in range(len(self.matrix))]
            return Matrix(matrix1)
        else:
            raise IncorrectSize("Error!!! Matrices have different sizes!!!\n")

    def __mul__(self, other):
        if len(self.matrix[0]) == len(other.get_matrix()):
            resultMatrix = [[0 for jterator in range(len(other.get_row(iterator)))] for iterator in
                            range(len(self.matrix))]
            for iterator in range(len(self.matrix)):
                for jterator in range(len(other.get_row(iterator))):
                    for kterator in range(len(other.get_matrix())):
                        resultMatrix[iterator][jterator] += self.matrix[iterator][kterator] * other.get_element(
                            kterator, jterator)
            return Matrix(resultMatrix)
        else:
            raise IncorrectSize("Error!!! Matrices have wrong sizes!!!\n")

    def getDeterminant(self):
        if len(self.matrix) == 1:
            determinant = self.matrix[0][0]
            return determinant
        elif len(self.matrix) == 2:
            determinant = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
            return determinant
        elif len(self.matrix) == 3:
            determinant = self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2] + \
                          self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0] + \
                          self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1] - \
                          self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0] - \
                          self.matrix[0][1] * self.matrix[1][0] * self.matrix[2][2] - \
                          self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]
            return determinant

    def invertible(self):
        result = [[0 for col in range(len(self.matrix[0]))] for row in range(len(self.matrix))]
        determinant = self.getDeterminant()
        if determinant == 0:
            raise ErrorDivision("determinant of the matrix = 0 \n")
        else:
            if len(self.matrix) == 1 and len(self.matrix[0]) == 1:
                first = self.matrix[0][0]
                result[0][0] = first
                return Matrix(result)

            elif len(self.matrix) == 2 and len(self.matrix[0]) == 2:
                first = self.matrix[1][1]
                second = -(self.matrix[0][1])
                third = -(self.matrix[1][0])
                fourth = self.matrix[0][0]
                invertMatrix = [[first, second], [third, fourth]]
                for iterator in range(len(invertMatrix)):
                    for jterator in range(len(invertMatrix[0])):
                        result[iterator][jterator] += round(invertMatrix[iterator][jterator] / determinant, 2)

            elif len(self.matrix) == 3 and len(self.matrix[0]) == 3:
                first = self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1]
                second = -(self.matrix[1][0] * self.matrix[2][2] - self.matrix[2][0] * self.matrix[1][2])
                third = self.matrix[1][0] * self.matrix[2][1] - self.matrix[1][1] * self.matrix[2][0]
                fourth = -(self.matrix[0][1] * self.matrix[2][2] - self.matrix[2][1] * self.matrix[0][2])
                fifth = self.matrix[0][0] * self.matrix[2][2] - self.matrix[0][2] * self.matrix[2][0]
                sixth = -(self.matrix[0][0] * self.matrix[2][1] - self.matrix[0][1] * self.matrix[2][0])
                seventh = self.matrix[0][1] * self.matrix[1][2] - self.matrix[0][2] * self.matrix[1][1]
                eighth = -(self.matrix[0][0] * self.matrix[1][2] - self.matrix[0][2] * self.matrix[1][0])
                ninth = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
                invertMatrix = [[first, fourth, seventh], [second, fifth, eighth], [third, sixth, ninth]]
                for iterator in range(len(invertMatrix)):
                    for jterator in range(len(invertMatrix[0])):
                        # print(invertMatrix[i][j])
                        result[iterator][jterator] += round(invertMatrix[iterator][jterator] / determinant, 2)
            return Matrix(result)

    def __truediv__(self, other):
        if len(self.matrix[0]) == len(other.get_matrix()):
            result = [[0 for col in range(len(other.matrix[0]))] for row in range(len(self.matrix))]
            invert = Matrix.invertible(other)
            for iterator in range(len(self.matrix)):
                for jterator in range(len(other.get_row(iterator))):
                    for kterator in range(len(other.matrix)):
                        result[iterator][jterator] += round(
                            self.matrix[iterator][kterator] * invert.matrix[kterator][jterator], 2)
            # print(invert.matrix)
            return Matrix(result)
        else:
            raise IncorrectSize("Error!!! Matrices have wrong sizes!!!\n")

    def __str__(self):
        line = ''
        for row in self.matrix:
            for element in row:
                line += str(element) + ' '
            line += "\n"
        return line
