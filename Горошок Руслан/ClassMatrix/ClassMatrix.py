class Matrix():
	
	
	def __init__(self , row , column):
		self.row = row
		self.column = column
		self.matrix = []
	
	
	def get_matrix(self,file_name):
		try:
			with open(file_name) as matrix_file:
				self.matrix = []
				for i in range(0, self.row):
					self.matrix.append(list(map(int,matrix_file.readline().split()[:self.column])))
		finally:
			matrix_file.close()
				
	def print_matrix(self):	
		for row in self.matrix:
			for column in row:
				print(column , end = " ")
			print(" ")
		print(" ")
	
			
	def __add__(self,other):
		try:
			if (len(self.matrix) == len(other.matrix)) and (len(self.matrix[0]) == len(other.matrix[0])):
				addMatrix = Matrix(self.row,self.column)
				addMatrix.matrix = []
				for iterator in range(self.row):
					newMatrix = []
					for jterator in range(self.column):
						newMatrix.append(int(self.matrix[iterator][jterator]) + int(other.matrix[iterator][jterator]))
					addMatrix.matrix.append(newMatrix)
			else:
				print("We can't add this matrix")
				addMatrix = Matrix(self.row,self.column)
			return addMatrix
		except IndexError :
			print("We can't add this matrix")
			addMatrix.matrix = []
			return addMatrix
	
	
	def __sub__(self,other):
		try:
			
			if (len(self.matrix) == len(other.matrix)) and (len(self.matrix[0]) == len(other.matrix[0])):
				subMatrix = Matrix(self.row,self.column)
				subMatrix.matrix = []
				for iterator in range(self.row):
					newMatrix = []
					for jterator in range(self.column):
						newMatrix.append(int(self.matrix[iterator][jterator]) - int(other.matrix[iterator][jterator]))
					subMatrix.matrix.append(newMatrix)
			else:
				print("We can't add this matrix")
				subMatrix = Matrix(self.row,self.column)
			return subMatrix
			
		except IndexError :
			print("We can't add this matrix")
			subMatrix.matrix = []
			return subMatrix
			
	def writeMatrixInFile(self):
		try:
			with open("resultMatrix.txt", "a+") as matrix_file:
				matrix_file.write("\n")
				for row in self.matrix:
					for column in row:
						matrix_file.write(str(column))
						matrix_file.write(" ")
					matrix_file.write(("\n"))		
		finally:
			matrix_file.close()
			
