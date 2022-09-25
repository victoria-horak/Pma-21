from Parser import ParseRow
from DifferentDimensionsException import DifferentDimensionsException

class Matrix:
    def __init__(self, _matrix=None):
        if (_matrix is None): 
            self.matrix = []
        else:
            self.matrix = _matrix
    def ReadFromFile(self, fileName):
        fileToReadFrom = open(fileName)
        lines = fileToReadFrom.readlines()
        for line in lines:
            currentRow = ParseRow(line)
            if (currentRow != []): self.matrix.append(currentRow)
    def WriteToFile(self, fileName):
        fileToWriteTo = open(fileName, "w")
        rowCount = self.matrix.__len__()
        for rowIterator in range(0, rowCount):
            currentLine = ''
            for element in self.matrix[rowIterator]:
                currentLine += str(element) + ' '
            fileToWriteTo.write(currentLine + '\n')
        fileToWriteTo.close()
    def __add__(self, other):
        resultMatrix = []
        rowCount1 = self.matrix.__len__()
        columnCount1 = self.matrix[0].__len__()
        rowCount2 = other.matrix.__len__()
        columnCount2 = other.matrix[0].__len__()
        
        if (rowCount1 != rowCount2 or columnCount1 != columnCount2):
            raise DifferentDimensionsException('Dimensions of two matrices are different')
        for rowIterator in range(0, rowCount1):
            currentRow = []
            for columnIterator in range(0, columnCount1):
                currentRow.append(int(self.matrix[rowIterator][columnIterator]) + int(other.matrix[rowIterator][columnIterator]))
            resultMatrix.append(currentRow)
        return Matrix(resultMatrix)
    def __sub__(self, other):
        resultMatrix = []
        rowCount1 = self.matrix.__len__()
        columnCount1 = self.matrix[0].__len__()
        rowCount2 = other.matrix.__len__()
        columnCount2 = other.matrix[0].__len__()
        if (rowCount1 != rowCount2 or columnCount1 != columnCount2):
            raise DifferentDimensionsException('Dimensions of two matrices are different')
        for rowIterator in range(0, rowCount1):
            currentRow = []
            for columnIterator in range(0, columnCount1):
                currentRow.append(int(self.matrix[rowIterator][columnIterator]) - int(other.matrix[rowIterator][columnIterator]))
            resultMatrix.append(currentRow)
        return Matrix(resultMatrix)