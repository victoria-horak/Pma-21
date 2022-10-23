class Vector(object):

    #конструктор
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    #Метод додавання
    def __add__ (self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    #Метод віднімання
    def __sub__ (self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    #Метод виведення
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    #Метод читання з файлу
    def readfromtxt(self, filename):
        with open(filename, 'r') as file:
            text = ''.join(file.read().split()) #Форматування стрінги(Отримуємо стрінгу і по індексах присвоюємо значення атрибутам)
            
        self.x = int(text[0]) #Присвоєння атрибутів
        self.y = int(text[1])
        self.z = int(text[2])

    #Метод вписування в файл
    def writeToTxt(self, filename):
        with open(filename, 'w') as file:
            file.write(f"{self.x} {self.y} {self.z}")

