from random import randint


class Matrix:
    # Конструктор(Приймає значення кількості рядків і колонок)
    def __init__(self, n, m):
        self.matrix = self.get_matrix(n, m)

    # Геттер для матриці
    def get_matrix(self, n, m):
        matrix = [[None for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = randint(1, 10) #Матриця наповнюється рандомними значеннями від 1 до 10
        return matrix

    # Для гарного виводу матриці
    def get_readable_matrix_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    # Для виводу матриці без застосування методів(через print())
    def __str__(self):
        return self.get_readable_matrix_string(self.matrix)

    # Метод додавання
    def __add__(self, secondMatrix):
        result = [[0 for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))] #Створюється пуста матриця

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + secondMatrix.matrix[i][j]

        return self.get_readable_matrix_string(result)

    # Метод віднімання
    def __sub__(self, secondMatrix):
        result = [[0 for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] - otsecondMatrixher.matrix[i][j]

        return self.get_readable_matrix_string(result)

    def readFromFile(self, fileName):
        self.matrix = []
        with open(fileName) as file:
            try:
                for line in file:
                    if not line.isspace():
                        line = line.split(",")
                        row = []
                        for columnIterator in range(0, len(line)):
                            element = int(line[columnIterator])
                            row.append(element)
                        self.matrix.append(row)
            except ValueError:
                print("wrong element type")
                self.matrix.clear()

    def printToFile(self, fileName, matrix):
        with open(fileName, "w") as file:
            file.write(matrix)


inputFile = Matrix(3, 3)                   #Cтворюємо матрицю
inputFile.readFromFile("matrixin.txt")     #Задаємо значення з файлу

m2 = Matrix(3,3)                   #Cтворюємо матрицю
m2.readFromFile("matrixin2.txt")   #Задаємо значення з файлу

inputFile.printToFile("matrixout.txt", m1 - m2)  #Сюди другим аргументом передати вираз
