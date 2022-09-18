import numpy as np

# Creating 2D array
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])

print('Array:\n', A)
print(" ")
print('Array:\n', B)
file = open("file2.txt", "w+")

content = str(np.subtract(A, B))
file.write(content)
file.close()

file = open("file2.txt", "r")
content = file.read()

print("\nContent in file2.txt:\n", content)
file.close()