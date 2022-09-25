from ClassVector import Vector

print("Print firstVector :")
firstVector = Vector(4)
firstVector.readDataFromFile("firstVector.txt")
firstVector.printVector()
firstVector.writeVectorInFile()

print("\nPrint secondVector :")
vector2 = Vector(4)
vector2.readDataFromFile("secondVector.txt")
vector2.printVector()

print("\nfirstVector + secondVector :")
addVector = firstVector + vector2
addVector.printVector()

print("\nfirstVector - secondVector :")
subVector = firstVector - vector2
subVector.printVector()
