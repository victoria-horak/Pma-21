class differLength(Exception): #для вип. різних довжин у векторах
    pass


class Vector:
    def __init__(self, len_vector):
        self.len_vector = len_vector
        self.vector = []

    def read_from_file(self, fileName):
        with open(fileName, 'r') as file:
            for i in range(0, self.len_vector):
                self.vector.append(int(file.readline().strip())) #strip - видаляє всі пробіли в тхт файлі

        return self.vector


    def print_vectors(self): #вивід векторів у консоль
        if self.vector != []:
            print("(" , end="")

            for i in range(0, self.len_vector):
                print(self.vector[i] - 1, end=",")

            print(self.vector[i], end=(",").rstrip(",") + ")")

        else:
            pass


    def write_result(self): #запис у файл результату
        try:
            with open("result_vector.txt", "a+") as result_vector:

                for i in range(0, self.len_vector):
                    result_vector.write(str(self.vector[i]))
                    result_vector.write(" ")
                result_vector.write("\n")

        finally: #обов'язково відбудеться після блоку try
            result_vector.close()


    def add_2_vectors(self, second): #додавання векторів
        if(len(self.vector) == len(second.vector)):
            res_vector = Vector(self.len_vector)
            res_vector.vector = [] #утворення результуючого вектора
            for iter in range(0, self.len_vector and second.len_vector):
                res_vector.vector.append(int(self.vector[iter]) + int(second.vector[iter]))

        else:
            res_vector = Vector(self.len_vector) #утворення результуючого вектора
            res_vector.vector = []
            print("Vectors cannot be added")

        return res_vector


    def substract_2_vectors(self, second): #віднімання 2 векторів
        if (len(self.vector) == len(second.vector)):
            res_vector = Vector(self.len_vector) #утворення результуючого вектора
            res_vector.vector = []
            for iter in range(0, self.len_vector and second.len_vector):
                res_vector.vector.append(int(self.vector[iter]) - int(second.vector[iter]))

        else:
            res_vector = Vector(self.len_vector)
            res_vector.vector = []  # утворення результуючого вектора
            print("Vectors cannot be added")

        return res_vector
