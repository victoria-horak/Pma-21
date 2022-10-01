from InvalidLengthException import InvalidLenghtException


class Matrix:
    def __init__(self, matrix=None):
        if matrix is None:
            matrix = []
        self.__matrix = matrix

    def __len__(self):
        return len(self.__matrix)

    def __getitem__(self, index):
        return self.__matrix[index]

    def read_matrix(self, file_name, column, row):
        with open(file_name, "r") as file:
            for line in file:
                list = [x for x in line.strip().split(",")]
                list = [int(x) for x in list if x]
                self.__matrix.append(list)
            self.__matrix = [x for x in self.__matrix if x]
            self.__matrix = [[self.__matrix[i][j] for j in range(0, row)] for i in range(0, column)]
        file.close()
        return self.__matrix

    @classmethod
    def read_matrix_static(cls, file_name, column, row):
        with open(file_name, "r") as file:
            matrix = []
            for line in file:
                list = [x for x in line.strip().split(",")]
                list = [int(x) for x in list if x]
                matrix.append(list)
            matrix = [x for x in matrix if x]
            result = []
            for iterator in range(0, column):
                rows = []
                for jterator in range(0, row):
                    rows.append(0)
                result.append(rows)
            for iterator in range(0, column):
                for jterator in range(0, row):
                    result[iterator][jterator] = matrix[iterator][jterator]
        file.close()
        return cls(result)

    @classmethod
    def add_matrix_static(cls, matrix1, matrix2):
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            result = [[matrix1[iterator][jterator] + matrix2[iterator][jterator] for jterator in
                       range(len(matrix1[0]))] for iterator in range(len(matrix2))]
            return cls(result)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    def __add__(self, other):
        if len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0]):
            matrix1 = [[self.__matrix[iterator][jterator] + other.__matrix[iterator][jterator] for jterator in
                        range(len(self.__matrix[0]))] for iterator in range(len(self.__matrix))]
            return Matrix(matrix1)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    @classmethod
    def sub_matrix_static(cls, matrix1, matrix2):
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            result = [[matrix1[iterator][jterator] - matrix2[iterator][jterator] for jterator in
                       range(len(matrix1[0]))] for iterator in range(len(matrix2))]
            return cls(result)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    def __sub__(self, other):
        if len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0]):
            matrix1 = [[self.__matrix[iterator][jterator] - other.__matrix[iterator][jterator] for jterator in
                        range(len(self.__matrix[0]))] for iterator in range(len(self.__matrix))]
            return Matrix(matrix1)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    @classmethod
    def add_matrix(cls, matrix1, matrix2):
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            matrix1 = [[matrix1[iterator][jterator] + matrix2[iterator][jterator] for jterator in
                        range(len(matrix1[0]))] for iterator in range(len(matrix1))]
            return cls(matrix1)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    def __str__(self):
        string = ''
        for iterator in self.__matrix:
            string += str(iterator) + '\n'
        return string

    def write_to_file(self, file_name):
        with open(file_name, 'a') as file:
            for iterator in self.__matrix:
                file.write(str(iterator) + '\n')
            file.write('\n')
        file.close()

    @classmethod
    def write_to_file_static(cls, file_name, matrix):
        with open(file_name, 'a') as file:
            for iterator in matrix:
                file.write(str(iterator) + '\n')
            file.write('\n')
        file.close()
