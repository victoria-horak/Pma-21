from Matrix import Matrix
from Vector import Vector
from Constants import PATH

resultFile = "result.txt"


def add_to_file(text, filePath=resultFile):
    with open(filePath, "a") as file:
        file.write(text)


with open(resultFile, "w") as file:
    file.write("")

matrix_first = Matrix().fromFile("Matrix.txt")
matrix_second = Matrix("""
1 0 3
0 5 0
7 0 9
""")


add_to_file("Matrix First:")
Matrix.toFile_Static(matrix_first, resultFile)
add_to_file("Matrix Second:")
matrix_second.toFile(resultFile)
# add_to_file("Matrix Multiplication:")
# (matrix_first / matrix_second).toFile(resultFile)
#print(matrix_second.det())
inversed_second = matrix_second.inverse()
print(inversed_second * matrix_second)
# matrix_second = Matrix.fromFile(Constants.PATH + "matrix.txt")


# add_to_file("Matrix First:")
# Matrix.toFile_Static(matrix_first, resultFile)
# add_to_file("Matrix Second:")
# matrix_second.toFile(resultFile)
# # +
# add_to_file("Addition")
# Matrix.add(matrix_first, matrix_second).toFile(resultFile)
# #(matrix_first + matrix_second).toFile(resultFile)
# # -
# add_to_file("Substraction")
# (matrix_first - matrix_second).toFile(resultFile)
# # transpose
# add_to_file("Transposition Second Matrix")
# matrix_second.transpose.toFile(resultFile)
# # Mult by -4
# add_to_file("Multiply First Matrix by -4")
# matrix_first.scalar_mult(-4).toFile(resultFile)
# # Remove 2 row and 1 column
# add_to_file("Remove 2 row and 1 column from First Matrix")
# matrix_first.subMatrix(1, 0).toFile(resultFile)

# Vectors
vector_first = Vector.fromFile("vector_second.txt")
vector_second = Vector.fromFile("vector.txt")

add_to_file("\n\n-------Vectors-----\n")
add_to_file("Vector First:")
vector_first.toFile(resultFile)
add_to_file("Vector Second:")
vector_second.toFile(resultFile)
# # +
# add_to_file("Addition")
# Vector.toFile_Static(vector_first + vector_second, resultFile)
# # -
# add_to_file("Substraction")
# (vector_first - vector_second).toFile(resultFile)
# Mult by 6
add_to_file("Multiply First Vector by Second vector")
(vector_first * vector_second).toFile(resultFile)
add_to_file("Divide First Vector by Second vector")
(vector_first / vector_second).toFile(resultFile)
