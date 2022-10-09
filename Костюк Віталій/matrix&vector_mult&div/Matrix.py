from DifferentSizesMatrix import *


class Matrix():
    def __init__(self, matrix):
        """Ініціаліщація"""
        self.matrix = matrix

    def __getitem__(self, i):
        return self.matrix[i]

    def __str__(self):
        """Конвертація в стрічку"""
        matrix_to_str = ''
        for iterator in self.matrix:
            matrix_to_str += str(iterator) + '\n'
        return matrix_to_str

    def __mul__(self, other):
        """Множення матриць"""
        if len(self.matrix) == len(other.matrix[0]):
            result_matrix = [[0 for col in range(len(other.matrix[0]))] for row in range(len(self.matrix))]
            for rows_of_first in range(len(self.matrix)):
                for col_of_second in range(len(other.matrix[rows_of_first])):
                    for iterator in range(len(other.matrix)):
                        result_matrix[rows_of_first][col_of_second] += \
                            self.matrix[rows_of_first][iterator] * other.matrix[iterator][col_of_second]
            return Matrix(result_matrix)
        else:
            raise DifferentSizesMatrix("\nMatrices cannot be mult\n")

    def __truediv__(self, other):
        """Ділення матриць"""
        result = [[0 for col in range(len(other.matrix[0]))] for row in range(len(self.matrix))]
        reversed_matrix = Matrix.revers(other)
        for rows_of_first in range(len(self.matrix)):
            for col_of_second in range(len(self.matrix[rows_of_first])):
                for iterator in range(len(self.matrix)):
                    result[rows_of_first][col_of_second] += \
                        self.matrix[rows_of_first][iterator] * reversed_matrix[iterator][col_of_second]
            return Matrix(result)
        else:
            raise DifferentSizesMatrix("\nMatrices cannot be divided\n")

    def read_matrix(self, file_name):
        """Зчитування з файлу"""
        with open(file_name, 'r') as file:
            for line in file:
                temp_matrix = [element for element in line.strip().split(",")]
                temp_matrix = [int(element) for element in temp_matrix if element]
                self.matrix.append(temp_matrix)
            self.matrix = [element for element in self.matrix if element]
        file.close()
        return self.matrix

    def write_to_file(self, file_name):
        """Записування в файл"""
        file = open(file_name, 'a')
        for iterator in self.matrix:
            file.write(str(iterator) + '\n')
        file.write('\n')
        file.close()

    def det(self):
        if len(self.matrix) == 3:
            determinant = self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2] + self.matrix[0][1] * \
                          self.matrix[1][2] * \
                          self.matrix[2][0] + self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1] - \
                          self.matrix[0][2] * \
                          self.matrix[1][1] * self.matrix[2][0] - self.matrix[0][1] * self.matrix[1][0] * \
                          self.matrix[2][2] - \
                          self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]
            return determinant
        elif len(self.matrix) == 2:
            determinant = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
            return determinant

    def revers(self):
        determinant = self.det()
        if determinant != 0:
            """Знаходимо алгебраїчні доповнення"""
            if len(self.matrix) == 3 and len(self.matrix[0]) == 3:
                first = self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1]
                second = -(self.matrix[0][1] * self.matrix[2][2] - self.matrix[2][1] * self.matrix[0][2])
                third = self.matrix[0][1] * self.matrix[1][2] - self.matrix[1][1] * self.matrix[0][2]
                fourth = -(self.matrix[1][0] * self.matrix[2][2] - self.matrix[2][0] * self.matrix[1][2])
                fifth = self.matrix[0][0] * self.matrix[2][2] - self.matrix[0][2] * self.matrix[2][0]
                sixth = -(self.matrix[0][0] * self.matrix[1][2] - self.matrix[1][0] * self.matrix[0][2])
                seventh = self.matrix[1][0] * self.matrix[2][1] - self.matrix[2][0] * self.matrix[1][1]
                eigthth = -(self.matrix[0][0] * self.matrix[2][1] - self.matrix[2][0] * self.matrix[0][1])
                nineth = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
                revers_matrix = [
                    [round(first / determinant, 2), round(second / determinant, 2), round(third / determinant, 2)],
                    [round(fourth / determinant, 2), round(fifth / determinant, 2), round(sixth / determinant, 2)],
                    [round(seventh / determinant, 2), round(eigthth / determinant, 2), round(nineth / determinant, 2)]]
                return Matrix(revers_matrix)
            elif len(self.matrix) == 2 and len(self.matrix[0]) == 2:
                first = self.matrix[1][1]
                second = -(self.matrix[0][1])
                third = -(self.matrix[1][0])
                fourth = self.matrix[0][0]
                revers_matrix = [[round(first / determinant, 2), round(second / determinant, 2)],
                                 [round(third / determinant, 2), round(fourth / determinant, 2)]]
                return Matrix(revers_matrix)
        else:
            raise DifferentSizesMatrix("Determinant of second matrix cannot be equal to 0")
