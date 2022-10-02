from lengthNotMatchExeption import LengthNotMatchExeption


class Vector:

    def __init__(self, vector=None):
        if vector is None:
            self.__vector = []
        else:
            self.__vector = vector

    @classmethod
    def readFromFile(cls, nameFile=""):
        with open(nameFile, "r") as file:
            vector = []
            for line in file.readlines():
                for x in line.strip().split(","):
                    vector.append(x)
            vector = [x for x in vector if x]
            vector = [int(x) for x in vector if x]
        return cls(vector)

    def __str__(self):
        result = ""
        for item in self.__vector:
            result += str(item) + " "
        result += "\n"
        return result

    def __add__(self, other):
        vectorResult = Vector()
        if len(self.__vector) != len(other.__vector):
            raise LengthNotMatchExeption("Vector length not match")
        for item in range(len(self.__vector)):
            vectorResult.__vector.append(self.__vector[item] + other.__matrix[item])
        return vectorResult

    def __sub__(self, other):
        vectorResult = Vector()
        if len(self.__vector) != len(other.__vector):
            raise LengthNotMatchExeption("Vector length not match")
        for item in range(len(self.__vector)):
            vectorResult.__vector.append(self.__vector[item] + other.__matrix[item])
        return vectorResult

    def writeToFile(self, nameFile):
        with open(nameFile, "a") as file:
            file.write(str(self))

    @classmethod
    def sum_vector(cls, vectorFirst, vectorSecond):
        vectorResult = Vector()
        if len(vectorFirst) != len(vectorSecond):
            raise LengthNotMatchExeption("Vector length not match")
        for item in range(len(vectorFirst)):
            vectorResult.__vector.append(vectorFirst[item] + vectorSecond[item])
        return cls(vectorResult)

    @classmethod
    def sub_vector(cls, vectorFirst, vectorSecond):
        vectorResult = Vector()
        if len(vectorFirst) != len(vectorSecond):
            raise LengthNotMatchExeption("Vector length not match")
        for item in range(len(vectorFirst)):
            vectorResult.__vector.append(vectorFirst[item] - vectorSecond[item])
        return cls(vectorResult)

    def __len__(self):
        return len(self.__vector)

    def __getitem__(self, key):
        return self.__vector[key]