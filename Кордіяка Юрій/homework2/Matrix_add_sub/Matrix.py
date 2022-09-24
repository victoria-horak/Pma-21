from InvalidLengthException import InvalidLenghtException


class Matrix:
    def __init__(self, matrix=None):
        if matrix is None:
            matrix = []
        self.__matrix = matrix

    def read_matrix(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                list = [x for x in line.strip().split(",")]
                list = [int(x) for x in list if x]
                self.__matrix.append(list)
            self.__matrix = [x for x in self.__matrix if x]
        file.close()
        return self.__matrix

    def __add__(self, other):
        if len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0]):
            matrix1 = [[self.__matrix[iterator][jterator] + other.__matrix[iterator][jterator] for jterator in
                        range(len(self.__matrix[0]))] for iterator in range(len(self.__matrix))]
            return Matrix(matrix1)
        else:
            raise InvalidLenghtException('the lengths of the matrices do not match')

    def __sub__(self, other):
        if len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0]):
            matrix1 = [[self.__matrix[iterator][jterator] - other.__matrix[iterator][jterator] for jterator in
                        range(len(self.__matrix[0]))] for iterator in range(len(self.__matrix))]
            return Matrix(matrix1)
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
