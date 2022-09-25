class differSize(Exception): #для вип. різних розмірів у матрицях
    pass


class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = []


    def Enter_Matrix(self, fileName):  # ввід з файлу
        with open(fileName, 'r') as file:
            matrix = [[int(element) for element in matrix_str.split(' ')] for matrix_str in file]
        return matrix


    def write(self, matrix, fileName):  # запис у файл результату
        file = open(fileName, 'a')
        for iter in matrix:
            file.write(str(iter) + '\n')


    def Add_2matrix(self, mat1, mat2, fileName):  # дод. 2 матриць
        if (len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
            file = open(fileName, 'a')
            file.write(str(differSize("Matrixes don`t have same size!")) + '\n')

            raise differSize("Matrixes don`t have same size!")

        else:
            res_matrix = []
            for iter in range(len(mat1)):
                row = []
                for jter in range(len(mat1[0])):
                    row.append(0)
                res_matrix.append(row)
        for iter in range(len(mat1)):
            for jter in range(len(mat1[0])):
                res_matrix[iter][jter] = mat1[iter][jter] + mat2[iter][jter]
        return res_matrix


    def Substract_2matrix(self, mat1, mat2, fileName):  # відн. 2 матриць
        if (len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
            file = open(fileName, 'a')
            file.write(str(differSize("Matrixes don`t have same size!")) + '\n')
            raise differSize("Matrixes don`t have same size!")

        else:
            res_matrix = []
            for iter in range(len(mat1)):
                row = []
                for jter in range(len(mat1[0])):
                    row.append(0)
                res_matrix.append(row)
        for iter in range(len(mat1)):
            for jter in range(len(mat1[0])):
                res_matrix[iter][jter] = mat1[iter][jter] - mat2[iter][jter]
        return res_matrix
