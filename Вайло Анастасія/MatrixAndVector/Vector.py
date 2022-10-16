from DifferentLengthsException import DifferentLengthsException

class Vector:
    def __init__(self, fileName, _vector = None):
        if (_vector is None):
            self.vector = Vector.read_from_file(fileName)
        else:
            self.vector = _vector


    def length(self):
        return self.vector.__len__()
    
    @staticmethod
    def read_from_file(fileName):
        result = []
        file = open(fileName, 'r')
        current_vector = file.readlines()
        for line in current_vector:
            line = line.strip()
            current_row = line.split(' ')
            current_row = list(filter((' ').__ne__, current_row))
            current_row = list(filter(('').__ne__, current_row))
            if (current_row != []): 
                for element in current_row:
                    result.append(element)
        return result
    def write_to_file(vector_to_print, fileName):
        line = ''
        for element in vector_to_print.vector:
            line += str(element) + ' '
        file = open(fileName, 'w')
        file.write(line)
    #adding two vectors
    def __add__(self, another):
        len1 = self.length()
        len2 = another.length()
        result = Vector('', [0 for i in range(self.length())])
        
        for iterator in range(self.length()):
            result.vector[iterator] = int(self.vector[iterator]) + int(another.vector[iterator])
        return result
    @staticmethod    
    def add_vectors(first_vector, second_vector):
        return first_vector + second_vector
    def add_vectors_non_static(self, another):
        return self + another
    #subtracting two vectors
    def __sub__(self, another):
        len1 = self.length()
        len2 = another.length()
        result = Vector('', [0 for i in range(self.length())])
        for iterator in range(self.length()):
            result.vector[iterator] = int(self.vector[iterator]) - int(another.vector[iterator])
        return result
    @staticmethod    
    def sub_vectors(first_vector, second_vector):
        return first_vector - second_vector
    def sub_vectors_non_static(self, another):
        return self - another
    #multiplication of two vectors
    def __mul__(self, another):
        result = 0
        if (self.length() != another.length()):
            raise DifferentLengthsException('Lengths are different')
        for i in range(self.length()):
            result += float(self.vector[i]) * float(another.vector[i])
        return result
    @staticmethod    
    def mul_vectors(first_vector, second_vector):
        return first_vector * second_vector
    def mul_vectors_non_static(self, another):
        return self * another
    #division of two vectors
    def __truediv__(self, another):
        result = Vector('', [0 for i in range(self.__len__())])
        if (self.length() != another.length()):
            raise DifferentLengthsException('Lengths are different')
        for i in range(self.__len__()):
            result.vector[i] = float(self.vector[i]) / float(another.vector[i])
    @staticmethod    
    def div_vectors(first_vector, second_vector):
        return first_vector / second_vector
    def div_vectors_non_static(self, another):
        return self / another
