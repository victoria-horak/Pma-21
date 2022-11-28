from LengthError import LengthErrorException
from ErrorDivision import ErrorDivision

class Vector:
    #Конструктор за замовчуванням
    def __init__(self, vector=None):
        if vector is None:
            vector = []
        self.__vector = vector

    #Зчитування вектору
    def read_vector(self, file_name):
        with open(file_name, "r") as file:
            list_for_vector = []
            #В t зберігаємо число, якщо зустрічаємо пробіл, то додаємо це число в вектор
            for line in file:
                t = ''
                for c in line:
                    if c != ' ':
                        t += c
                    elif t != '':
                        list_for_vector.append(int(t))
                        t = ''
                if t != '':
                    list_for_vector.append(int(t))
            self.__vector = list_for_vector
        return self.__vector

    # Поелементно перемножуємо елементи двох векторів, якщо розміри не співпадають - то видаємо помилку
    def __mul__(self, other):
        if len(self.__vector) != len(other.__vector):
            raise LengthErrorException("vectors have different sizes\n")
        else:
            vector = [self.__vector[iterator] * other.__vector[iterator] for iterator in range(len(self.__vector))]
            return Vector(vector)

    # Поелементно ділимо елементи двох векторів, якщо розміри не співпадають - то видаємо помилку
    def __truediv__(self, other):
        for el in other.__vector:
            if el == 0:
                raise ErrorDivision("division by 0")
        vector = [self.__vector[iterator] / other.__vector[iterator] for iterator in range(len(self.__vector))]
        return Vector(vector)

    #Вивід вектору до файлу
    def write_to_file(self, file_name):
        with open(file_name, 'a') as file:
            for iterator in self.__vector:
                file.write(str(iterator) + '\n')
            file.write('\n')

    def __str__(self):
        string = ''
        for iterator in self.__vector:
            string += str(iterator) + '\n'
        return string
