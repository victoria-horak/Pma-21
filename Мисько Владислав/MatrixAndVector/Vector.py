from Parser import ParseRow
from DifferentLengthsException import DifferentLengthsException

class Vector:
    def __init__(self, vector=None):
        if (vector is None):
            self.vector = []
        else:
            self.vector = vector
    def ReadFromFile(self, fileName):
        with open(fileName) as fileToReadFrom:
            lines = fileToReadFrom.readlines()
            if (lines.__len__() > 1):
                for line in lines:
                    currentRow = ParseRow(line)
                    if (currentRow == []): continue
                    self.vector.append(int(currentRow[0]))
            else:
               self.vector = ParseRow(lines[0])
    def WriteToFile(self, fileName):
        with open(fileName, "w") as fileToWriteTo:
            fileToWriteTo.write(str(self))
    def __add__(self, other):
        resultVector = []
        
        if (self.vector.__len__() != other.vector.__len__()):
            raise DifferentLengthsException('Lengths of vectors are different')
        
        for iterator in range(0, self.vector.__len__()):
            resultVector.append(int(self.vector[iterator]) + int(other.vector[iterator]))
        return Vector(resultVector)
    def __sub__(self, other):
        resultVector = []
        if (self.vector.__len__() != other.vector.__len__()):
            raise DifferentLengthsException('Lengths of vectors are different')
        for iterator in range(0, self.vector.__len__()):
            resultVector.append(int(self.vector[iterator]) - int(other.vector[iterator]))
        return Vector(resultVector)
    def __str__(self):
        result = ''
        for element in self.vector:
            result += str(element) + ' '
        return result