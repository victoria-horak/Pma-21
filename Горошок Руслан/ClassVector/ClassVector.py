class Vector():
	
	def __init__(self, sizeVector):
		self.vector = []
		self.sizeVector = sizeVector
		
	def readDataFromFile(self, file_name):
		with open(file_name , 'r') as f:
			for i in range(0,self.sizeVector):
				self.vector.append(int(f.readline().strip()))
		return self.vector
		
	def printVector(self):
		if self.vector != []:
			print("(" , end = "")
			for i in range(0,self.sizeVector):
				print(self.vector[i] - 1 , end = ",")	
			print(self.vector[i] , end = (",").rstrip(",") + ")")
		else:
			pass
		
		
	def __add__(self,other):
		if(len(self.vector) == len(other.vector)):
			addVector = Vector(self.sizeVector)
			addVector.vector = []
			for i in range(0,self.sizeVector and other.sizeVector):
				addVector.vector.append(int(self.vector[i]) + int(other.vector[i]))
		else:
			addVector = Vector(self.sizeVector)
			addVector.vector = []
			print("we cannot add this vector")
		return addVector
	
	def __sub__(self , other):
		if(len(self.vector) == len(other.vector)):
			subVector = Vector(self.sizeVector)
			subVector.vector = []
			for i in range(0,self.sizeVector and other.sizeVector):
				subVector.vector.append(int(self.vector[i]) - int(other.vector[i]))
		else:
			subVector = Vector(self.sizeVector)
			subVector.vector = []
			print("We cannot sub this vector")
		return subVector
	
	def writeVectorInFile(self):
		try:
			with open("resultVector.txt", "a+") as vector_file:
				for i in range(0,self.sizeVector):
					vector_file.write(str(self.vector[i]))
					vector_file.write(" ")
				vector_file.write("\n")
		finally:
			vector_file.close()
