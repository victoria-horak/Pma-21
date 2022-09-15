import re

path = './Батьків Нестор/Matrix Addition/'

def stringToMatrix(string):
 height = string.count("\n")  + 1
 readList = re.sub("\s+"," ",string).split(" ")
 length = len(readList) /height
 matrix = []
 iterator = 0
 row = []
 for element in readList:
    row.append(element)
    iterator+= 1
    if iterator >= length:
        iterator = 0
        matrix.append(row)
        row = [] 
 return matrix

def matrixAddition(matrix1,matrix2):
    print(len(matrix1) )
    if(len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0])  ):
     raise ValueError("Matrixes have diffrent dimensions")
    resultMatrix = []
    iteratorI = 0
    for matrix1row in matrix1:
        row = []
        iteratorJ = 0
        for matrix1elem in matrix1row:
            row.append(int(matrix1elem) + int(matrix2[iteratorI][iteratorJ]))
            iteratorJ+=1
        resultMatrix.append(row)
        iteratorI+=1
    return resultMatrix

def matrixToString(matrix):
    string = ""
    for row in matrix:
        for elem in row:
            string += str(elem) + " "
        string +="\n"
    return string

def writeToFile(text,filePath):
 file = open(filePath, "w")
 file.write(text)
 file.close()


matrix1 = stringToMatrix(open(path+'matrix.txt').read())
matrix2 = stringToMatrix(open(path+'matrix2.txt').read())
try:
 writeToFile("Matrix1:\n"+matrixToString(matrix1)+
                  "\nMatrix2:\n"+matrixToString(matrix2)+
                  "\nResult Matrix:\n"+matrixToString(matrixAddition(matrix1,matrix2)),
                  path+"resultMatrix.txt")
except ValueError as e:
    print(e)
