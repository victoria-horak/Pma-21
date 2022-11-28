from Matrix import Matrix
from Vector import Vector
from LengthError import LengthErrorException

try:
     firstMatrix = Matrix()  # Створюємо першу матрицю
     secondMatrix = Matrix()  # Створюємо другу матрицю
     firstMatrix.read_matrix("Matrix.txt")  # Зчитую першу матрицю
     secondMatrix.read_matrix("Matrix1.txt")  # Зчитую другу матрицю
     print(firstMatrix, "\n")
     print(secondMatrix)
     multMatrix = firstMatrix * secondMatrix  # Матриця отримана після перемноження
     multMatrix.write_to_file("ResultMatrix.txt")  # Вивід цієї матриці до файлу
     divMatrix = firstMatrix  / secondMatrix  # Матриця отримана після ділення
     divMatrix.write_to_file("ResultMatrix.txt")  # Вивід цієї матриці до файлу
except LengthErrorException as e:
     print(str(e))
     fileResult = open("ResultMatrix.txt", "a")
     fileResult.write(str(e))

try:
     firstVector = Vector() # Створюємо перший вектор
     secondVector = Vector() #Створюємо другий вектор
     firstVector.read_vector("Vector1.txt") # Зчитуємо перший вектор
     secondVector.read_vector("Vector2.txt") #Зчитуємо другий вектор
     resultMultVector = firstVector * secondVector # Вектор отриманий після перемноження
     resultDicVector = firstVector / secondVector #Вектор отриманий після ділення
     resultMultVector.write_to_file("ResultVector.txt") # Вивід вектору після перемноження до файлу
     resultDicVector.write_to_file("ResultVector.txt") #Вивід вектору після ділення до файлу

except Exception as e:
     print(str(e))
     fileResult = open("ResultVector.txt", "a")
     fileResult.write(str(e))



