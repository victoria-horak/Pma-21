from LengthError import LengthErrorException
from ErrorDivision import ErrorDivision


class Matrix:
    # Конструктор за замовчуванням
    def __init__(self, matrix=None):
        if matrix is None:
            matrix = []
        self.__matrix = matrix

    # Зчитування матриці
    def read_matrix(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                row = []
                # В t зберігаємо число, якщо зустрічаємо пробіл, то додаємо це число в матрицю
                t = ''
                for c in line:
                    if c != ' ':
                        t += c
                    elif t != '':
                        row.append(int(t))
                        t = ''
                if t != '':
                    row.append(int(t))
                self.__matrix.append(row)
            self.__matrix = [x for x in self.__matrix if x]
        file.close()
        return self.__matrix

    # Перемножуємо дві матриці за принципом рядок на стовпчик, якщо довжина рядка першої матриці не дорівнює
    # кількості рядків другої матриці - то повертаємо повідомлення про помилку
    def __mul__(self, other):
        if len(self.__matrix[0]) != len(other.__matrix):
            raise LengthErrorException(
                "the number of elements in the row of the first matrix is not equal to the number of elements in the column of the second\n")
        else:
            result = [[0 for col in range(len(other.__matrix[0]))] for row in range(len(self.__matrix))]
            for i in range(len(self.__matrix)):
                for j in range(len(other.__matrix[0])):
                    for k in range(len(other.__matrix)):
                        result[i][j] += self.__matrix[i][k] * other.__matrix[k][j]
            return Matrix(result)

    def __str__(self):
        string = ''
        for iterator in self.__matrix:
            string += str(iterator) + '\n'
        return string

    # Вивід матриці до файлу
    def write_to_file(self, file_name):
        with open(file_name, 'a') as file:
            for iterator in self.__matrix:
                file.write(str(iterator) + '\n')
            file.write('\n')

    # Функція яка рахує визначник матриці. Розрахунок відбувається для матриці розміром 1...3
    def det(self):
        determinant = 0
        if len(self.__matrix) == 3:
            determinant = self.__matrix[0][0] * self.__matrix[1][1] * self.__matrix[2][2] + self.__matrix[0][1] * \
                          self.__matrix[1][2] * \
                          self.__matrix[2][0] + self.__matrix[0][2] * self.__matrix[1][0] * self.__matrix[2][1] - \
                          self.__matrix[0][2] * \
                          self.__matrix[1][1] * self.__matrix[2][0] - self.__matrix[0][1] * self.__matrix[1][0] * \
                          self.__matrix[2][2] - \
                          self.__matrix[0][0] * self.__matrix[1][2] * self.__matrix[2][1]
            return determinant
        elif len(self.__matrix) == 2:
            determinant = self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[1][0] * self.__matrix[0][1]
            return determinant
        elif len(self.__matrix) == 1:
            determinant += self.__matrix[0][0]
            return determinant

    # Функція яка для матриці повертає її обернену
    def obernena(self):
        result = [[0 for col in range(len(self.__matrix[0]))] for row in range(len(self.__matrix))]
        determinant = self.det()
        # тут зробити ерорку детермінанту
        if determinant == 0:
            raise ErrorDivision("determinant of the matrix = 0 \n")
        else:
            if len(self.__matrix) == 3 and len(self.__matrix[0]) == 3:
                first = self.__matrix[1][1] * self.__matrix[2][2] - self.__matrix[1][2] * self.__matrix[2][1]
                second = -(self.__matrix[0][1] * self.__matrix[2][2] - self.__matrix[2][1] * self.__matrix[0][2])
                third = self.__matrix[0][1] * self.__matrix[1][2] - self.__matrix[1][1] * self.__matrix[0][2]
                fourth = -(self.__matrix[1][0] * self.__matrix[2][2] - self.__matrix[2][0] * self.__matrix[1][2])
                fifth = self.__matrix[0][0] * self.__matrix[2][2] - self.__matrix[0][2] * self.__matrix[2][0]
                sixth = -(self.__matrix[0][0] * self.__matrix[1][2] - self.__matrix[1][0] * self.__matrix[0][2])
                seventh = self.__matrix[1][0] * self.__matrix[2][1] - self.__matrix[2][0] * self.__matrix[1][1]
                eigthth = -(self.__matrix[0][0] * self.__matrix[2][1] - self.__matrix[2][0] * self.__matrix[0][1])
                nineth = self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[1][0] * self.__matrix[0][1]
                obernenaMatrix = [[first, second, third], [fourth, fifth, sixth], [seventh, eigthth, nineth]]
                for i in range(len(obernenaMatrix)):
                    for j in range(len(obernenaMatrix[0])):
                        result[i][j] += round(obernenaMatrix[i][j] / determinant, 2)
            elif len(self.__matrix) == 2 and len(self.__matrix[0]) == 2:
                first = self.__matrix[1][1]
                second = -(self.__matrix[0][1])
                third = -(self.__matrix[1][0])
                fourth = self.__matrix[0][0]
                obernenaMatrix = [[first, second], [third, fourth]]
                for i in range(len(obernenaMatrix)):
                    for j in range(len(obernenaMatrix[0])):
                        result[i][j] += round(obernenaMatrix[i][j] / determinant, 2)
            elif len(self.__matrix) == 1 and len(self.__matrix[0]) == 1:
                first = self.__matrix[0][0]
                result[0][0] = first
            return Matrix(result)

    def __getitem__(self, x):
        return self.__matrix[x]

    # Ділення матртиці на матриці. За принципом множення першої матриці на обернену другу матрицю
    def __truediv__(self, other):
        if len(self.__matrix) > 3 or len(self.__matrix[0]) > 3:
            raise ErrorDivision("do not calculate the matrix of this size \n")
        else:
            result = [[0 for col in range(len(other.__matrix[0]))] for row in range(len(self.__matrix))]
            obernenaMatrix = Matrix.obernena(other)
            for i in range(len(self.__matrix)):
                for j in range(len(obernenaMatrix[0])):
                    for k in range(len(other.__matrix)):
                        result[i][j] += round(self.__matrix[i][k] * obernenaMatrix[k][j])
            return Matrix(result)
