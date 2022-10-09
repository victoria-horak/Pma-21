from error_size1 import Error_size


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def read_matrix_from_file(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                read_matrix = [element for element in line.replace(" ", "").replace("\n", "")]
                read_matrix = [float(element) for element in read_matrix]
                self.matrix.append(read_matrix)
            self.matrix = [element for element in self.matrix if element]
        file.close()
        return self.matrix

    def __mul__(self, other):
        if len(self.matrix[0])==len(other.matrix):

          result = [[0 for j in range(len(other.matrix[i]))] for i in range(len(self.matrix))]
          for i in range(len(self.matrix)):
              for j in range(len(other.matrix[0])):
                  for k in range(len(other.matrix)):
                      result[i][j] += self.matrix[i][k] * other.matrix[k][j]
          return Matrix(result)
        else:
            raise Error_size("Error!!! Matrices have different sizes!!!\n")

    # def det(self):
    #     if len(self.matrix) == 3:
    #         determinant = self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2] + self.matrix[0][1] * \
    #                       self.matrix[1][2] * \
    #                       self.matrix[2][0] + self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1] - \
    #                       self.matrix[0][2] * \
    #                       self.matrix[1][1] * self.matrix[2][0] - self.matrix[0][1] * self.matrix[1][0] * \
    #                       self.matrix[2][2] - \
    #                       self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]
    #         return determinant
    #     elif len(self.matrix) == 2:
    #         determinant = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
    #         return determinant
    #
    #
    # def inversion(self, other):
    #     determinant=self.det()
    #     result=[]
    #     determinant = self.det()
    #     if determinant != 0:
    #
    #         if len(self.matrix) == 3 and len(self.matrix[0]) == 3:
    #             first = self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1]
    #             second = -(self.matrix[0][1] * self.matrix[2][2] - self.matrix[2][1] * self.matrix[0][2])
    #             third = self.matrix[0][1] * self.matrix[1][2] - self.matrix[1][1] * self.matrix[0][2]
    #             fourth = -(self.matrix[1][0] * self.matrix[2][2] - self.matrix[2][0] * self.matrix[1][2])
    #             fifth = self.matrix[0][0] * self.matrix[2][2] - self.matrix[0][2] * self.matrix[2][0]
    #             sixth = -(self.matrix[0][0] * self.matrix[1][2] - self.matrix[1][0] * self.matrix[0][2])
    #             seventh = self.matrix[1][0] * self.matrix[2][1] - self.matrix[2][0] * self.matrix[1][1]
    #             eighth = -(self.matrix[0][0] * self.matrix[2][1] - self.matrix[2][0] * self.matrix[0][1])
    #             nineth = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
    #             revers_matrix = [
    #                 [round(first / determinant, 2), round(second / determinant, 2), round(third / determinant, 2)],
    #                 [round(fourth / determinant, 2), round(fifth / determinant, 2), round(sixth / determinant, 2)],
    #                 [round(seventh / determinant, 2), round(eighth / determinant, 2), round(nineth / determinant, 2)]]
    #             return Matrix(revers_matrix)
    #         elif len(self.matrix) == 2 and len(self.matrix[0]) == 2:
    #             first = self.matrix[1][1]
    #             second = -(self.matrix[0][1])
    #             third = -(self.matrix[1][0])
    #             fourth = self.matrix[0][0]
    #             revers_matrix = [[round(first / determinant, 2), round(second / determinant, 2)],
    #                              [round(third / determinant, 2), round(fourth / determinant, 2)]]
    #             return Matrix(revers_matrix)
    #     else:
    #         raise Error_size("!!!det=0!!!We can`t do division!!!")
    #
    # def __truediv__(self, other):
    #     result = [[0 for col in range(len(other.matrix[0]))] for row in range(len(self.matrix))]
    #     inversed_matrix = Matrix.inversion(self,other)
    #     for rows_of_first in range(len(self.matrix)):
    #         for col_of_second in range(len(self.matrix[rows_of_first])):
    #             for iterator in range(len(self.matrix)):
    #                 result[rows_of_first][col_of_second] += \
    #                     self.matrix[rows_of_first][iterator] * inversed_matrix[iterator][col_of_second]
    #         return Matrix(result)




    def __str__(self):
        line = ''
        for row in self.matrix:
            for element in row:
                line += str(element) + ' '
            line += "\n"
        return line