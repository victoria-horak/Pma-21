def ParseRow(thelist):
    array = []
    currentNumber = 0
    for element in thelist:
        if (element != ' ' and element != '\n'):
            currentNumber *= 10
            currentNumber += int(element)
        else: 
            array.append(int(currentNumber))
            currentNumber = 0
    if (thelist[thelist.__len__() - 1] != '\n'):
        array.append(currentNumber)
    return array

file1 = open("matrix1.txt")
file2 = open("matrix2.txt")
file3 = open("matrix3.txt", "w")

lines = file1.readlines()

matrix1 = []

for line in lines: 
    matrix1.append(ParseRow(line))

lines = file2.readlines()

matrix2 = []

for line in lines: 
    matrix2.append(ParseRow(line))

matrix3 = []

rowCount1 = len(matrix1)
columnCount1 = len(matrix1[0])

rowCount2 = len(matrix2)
columnCount2 = len(matrix2[0])

try:
    if (rowCount1 != rowCount2 or columnCount1 != columnCount2):
        raise Exception
except Exception:
    file3.write('Dimensions are different')
    file3.close()
    exit()

for rowIterator in range(0, rowCount1):
    currentRow = []
    for columnIterator in range(0, columnCount1):
        currentRow.append(int(matrix1[rowIterator][columnIterator]) + int(matrix2[rowIterator][columnIterator]))
    matrix3.append(currentRow)

for rowIterator in range(0, rowCount1):
    currentLine = ''
    for element in matrix3[rowIterator]:
        currentLine += str(element) + ' '
    file3.write(currentLine + "\n")
file3.close()