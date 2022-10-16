class Matrix:
    def __init__(self, fileName, _matrix = None):
        if (_matrix is None):
            self.matrix = Matrix.read_from_file(fileName)
        else:
            self.matrix = _matrix
    def rows_count(self):
        return self.matrix.__len__()
    def columns_count(self):
        return self.matrix[0].__len__()
    @staticmethod
    def read_from_file(fileName):
        result = []
        file = open(fileName, 'r')
        current_matrix = file.readlines()
        for line in current_matrix:
            line = line.strip()
            current_row = line.split(' ')
            current_row = list(filter((' ').__ne__, current_row))
            current_row = list(filter(('').__ne__, current_row))
            if (current_row != []): result.append(current_row)
        return result
    def write_to_file(matrix_to_print, fileName):
        result = ''
        for row_iterator in range(matrix_to_print.rows_count()):
            for column_iterator in range(matrix_to_print.columns_count()):
                result += str(matrix_to_print.matrix[row_iterator][column_iterator]) + ' '
            result += '\n'
        file = open(fileName, 'w')
        file.write(result)
    #adding two matrices
    def __add__(self, another):
        rows_first = self.rows_count()
        rows_second = another.rows_count()
        columns_first = self.columns_count()
        columns_second = another.columns_count()
        if (rows_first != rows_second or columns_first != columns_second):
            raise Exception('Different dimensions')
        result = self
        for row_iterator in range(rows_first):
            for column_iterator in range(columns_first):
                result.matrix[row_iterator][column_iterator] = int(self.matrix[row_iterator][column_iterator]) + int(another.matrix[row_iterator][column_iterator])
        return result
    @staticmethod    
    def add_matrices(first_matrix, second_matrix):
        return first_matrix + second_matrix
    def add_matrices_non_static(self, another):
        return self + another
    #subtracting two matrices
    def __sub__(self, another):
        rows_first = self.rows_count()
        rows_second = another.rows_count()
        columns_first = self.columns_count()
        columns_second = another.columns_count()
        if (rows_first != rows_second or columns_first != columns_second):
            raise Exception('Different dimensions')
        result = self
        for row_iterator in range(rows_first):
            for column_iterator in range(columns_first):
                result.matrix[row_iterator][column_iterator] = int(self.matrix[row_iterator][column_iterator]) - int(another.matrix[row_iterator][column_iterator])
        return result
    @staticmethod    
    def sub_matrices(first_matrix, second_matrix):
        return first_matrix - second_matrix
    def sub_matrices_non_static(self, another):
        return self - another
    #multiplication of two matrices
    @staticmethod
    def init_empty(rows, columns):
        result = Matrix('', [[0 for j in range(columns)] for i in range(rows)])
        for i in range(rows):
            for j in range(columns):
                result.matrix[i][j] = 0
        return result
    def __mul__(self, another):
        rows_first = self.rows_count()
        rows_second = another.rows_count()
        columns_first = self.columns_count()
        columns_second = another.columns_count()
        if (columns_first != rows_second):
            raise Exception('Invalid dimensions')
        result = Matrix.init_empty(rows_first, columns_second)
        for i in range(rows_first):
            for j in range(columns_second):
                for k in range(columns_second):
                    result.matrix[i][j] += int(self.matrix[i][k]) * int(another.matrix[k][j])
        return result
    @staticmethod    
    def mul_matrices(first_matrix, second_matrix):
        return first_matrix * second_matrix
    def mul_matrices_non_static(self, another):
        return self * another
    #division of two matrices
    def transponate(self):
        result = Matrix.init_empty(self.columns_count(), self.rows_count())
        for i in range(self.rows_count()):
            for j in range(self.columns_count()):
                result.matrix[j][i] = self.matrix[i][j]
        return result
    def __truediv__(self, another):
        return self * another.transponate()
    @staticmethod    
    def div_matrices(first_matrix, second_matrix):
        return first_matrix / second_matrix
    def div_matrices_non_static(self, another):
        return self / another