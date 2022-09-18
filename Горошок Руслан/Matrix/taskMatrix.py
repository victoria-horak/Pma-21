file_name = open("MatrixOne.txt")
file_name2 = open('MatrixTwo.txt')
file_name3 = open('ResultAddMatrix.txt','w')

matrix , matrix2,result = [],[],[]
max_length = 3
while True:
	try:
		length = int(input("Input length matrix1: "))
		assert length <= max_length
		break
	except AssertionError:
		print("MaxLength cannot be greater than the maximum length of the matrix in file")
		continue
		
for rowIterator in range(length):
	row = []
	for columnIterator in range(length):
		row.append(int(file_name.read(1))) 
	matrix.append(row)

for mat in matrix:
	print(mat)
print('\n')

while True:
	try:
		length2 = int(input("Input length matrix2: "))
		assert length2 <= max_length
		break
	except AssertionError:
		print("MaxLength cannot be greater than the maximum length of the matrix in file")
		continue
		
for rowIterator2 in range(length2):
	row2 = []
	for columnIterator2 in range(length2):
		row2.append(int(file_name2.read(1)))
	matrix2.append(row2)		

for mat2 in matrix2:
	print(mat2)
print('\n')

try:
	assert len(matrix) == len(matrix2)
	for iterator in range(len(matrix)):
		result.append([]) 
		for jterator in range(len(matrix[0])):
			result[iterator].append(matrix[iterator][jterator] + matrix2[iterator][jterator])
except AssertionError:
	file_name3.write("We can't add this matrix")

for res in result:
	file_name3.write(str(res))
	file_name3.write("\n")

file_name.close()

file_name2.close()

file_name3.close()
