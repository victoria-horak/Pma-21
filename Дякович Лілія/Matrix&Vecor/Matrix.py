from LengthError import LengthErrorException


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
        if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[0]) != len(other.__matrix[0]):
            raise LengthErrorException("matrices have different sizes")
        else:
            result = Matrix()
            result.__matrix = []
            for i in range(len(self.__matrix)):
                col = []
                for j in range(len(self.__matrix[i])):
                    col.append(self.__matrix[i][j] + other.__matrix[i][j])
                result.__matrix.append(col)
            return result

    @classmethod
    def add_matrix(cls, matrix1=None, matrix2=None):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise LengthErrorException("matrices have different sizes\n")
        else:
            result = []
            for i in range(len(matrix1)):
                col = []
                for j in range(len(matrix2[i])):
                    col.append(matrix1[i][j] + matrix2[i][j])
                result.append(col)
            return cls(result)

    def __sub__(self, other):
        if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[0]) != len(other.__matrix[0]):
            raise LengthErrorException("matrices have different sizes\n")
        else:
            result = Matrix()
            result.__matrix = []
            for i in range(len(self.__matrix)):
                col = []
                for j in range(len(self.__matrix[i])):
                    col.append(self.__matrix[i][j] - other.__matrix[i][j])
                result.__matrix.append(col)
            return result

    @classmethod
    def sub_matrix(cls, matrix1=None, matrix2=None):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise LengthErrorException("matrices have different sizes")
        else:
            result = []
            for i in range(len(matrix1)):
                col = []
                for j in range(len(matrix2[i])):
                    col.append(matrix1[i][j] - matrix2[i][j])
                result.append(col)
            return cls(result)

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
