from ClassMatrix import Matrix

print("print matrixFirst")
matrixFirst = Matrix(3,3)
matrixFirst.get_matrix("FirstMatrix.txt")
matrixFirst.print_matrix()
matrixFirst.writeMatrixInFile()

print("print MatrixSecond")
matrixSecond = Matrix(3,3)
matrixSecond.get_matrix("SecondMatrix.txt")
matrixSecond.print_matrix()

print("Result add MatrixFirst + MatrixSecond")
matrixAdd = matrixFirst + matrixSecond
matrixAdd.print_matrix()

print("Result substract MatrixFirst - MatrixSecond")
matrixSubstract = matrixFirst-matrixSecond
matrixSubstract.print_matrix()

