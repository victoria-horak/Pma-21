from ExceptionsVector import *
import sys

class Vector:
    pass

class Vector:

    def __len__(self):
        return len(self.vector)

    def returnVector(self):
        return self.vector

    def element(self, iterator):
        return self.vector[iterator]

    def __init__(self, vector = None):
        if vector== None:
            self.vector=[]
        elif type(vector) == int or type(vector) == float or type(vector) == chr or type(vector) == str:
            raise NotVecto('not vector')
        else:
            self.vector=vector

    def fillFromFile(self, fileName):
        file = open(fileName)
        lines = file.readlines()
        for rowIterator in range(0, len(lines)):
            line = lines[rowIterator].split(",")
            for columnsIterator in range(0, len(line)):
                try:
                    if line[0] == "\n":
                        break
                    element = int(line[columnsIterator])
                    self.vector.append(element)
                except ValueError as exc:
                    print("Error: "+str(exc))
                    sys.exit(1)
        file.close()

    @classmethod
    def fillFromFileStatic(self, fileName):
        file = open(fileName)
        vector =[]
        lines = file.readlines()
        for rowIterator in range(0, len(lines)):
            line = lines[rowIterator].split(",")
            for columnsIterator in range(0, len(line)):
                try:
                    if line[0] == "\n":
                        break
                    element = int(line[columnsIterator])
                    vector.append(element)
                except ValueError as exc:
                    print("Error: "+str(exc))
                    sys.exit(1)
        file.close()
        return Vector(vector)

    def __add__(self, other:Vector()):
        if len(self.vector) != len(other.vector):
            raise IfVectorsAreNotSameSize('we can\'t add this two vectors(not same length).')
        vector = []
        for rowIterator in range(0, len(self.vector)):
            vector.append(self.vector[rowIterator]+other.vector[rowIterator])
        return Vector(vector)

    @classmethod
    def add(cls, firstVector:Vector(), secondVector:Vector()):
        if len(firstVector.vector) != len(secondVector.vector):
            raise IfVectorsAreNotSameSize('we can\'t add this two vectors(not same length).')
        vector = []
        for rowIterator in range(0, len(firstVector.vector)):
            vector.append(firstVector.vector[rowIterator]+secondVector.vector[rowIterator])
        return Vector(vector)

    def __sub__(self, other:Vector()):
        if len(self.vector) != len(other.vector):
            raise IfVectorsAreNotSameSize('we can\'t add this two vectors(not same length).')
        vector = []
        for rowIterator in range(0, len(self.vector)):
            vector.append(self.vector[rowIterator]-other.vector[rowIterator])
        return Vector(vector)

    @classmethod
    def sub(cls, firstVector:Vector(), secondVector:Vector()):
        if len(firstVector.vector) != len(secondVector.vector):
            raise IfVectorsAreNotSameSize('we can\'t add this two vectors(not same length).')
        vector = []
        for rowIterator in range(0, len(firstVector.vector)):
            vector.append(firstVector.vector[rowIterator]-secondVector.vector[rowIterator])
        return Vector(vector)

    def show(self):
        if len(self.vector)==0:
            raise IfLengthIsZero('vector size is 0.')
        print(self.vector)

    @classmethod
    def showStatic(cls, vector:Vector()):
        if len(vector)==0:
            raise IfLengthIsZero('vector size is 0.')
        print(vector.returnVector())

    def fillFileWithVector(self, file):
        if len(self.vector) == 0:
            raise IfLengthIsZero('vector size is 0.')
        file.write(str(self.vector))
        file.write("\n")

    @classmethod
    def fillFileWithVectorStatic(cls, vector:Vector(), file):
        if len(vector) == 0:
            raise IfLengthIsZero('vector size is 0.')
        file.write("[")
        for iterator in range(0,len(vector)):
            if iterator == len(vector)-1:
                file.write(str(vector.element(iterator)))
            else:
                file.write(str(vector.element(iterator)) + ", ")
        file.write("]\n")