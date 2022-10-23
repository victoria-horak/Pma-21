from vector import Vector

x = Vector(1,2,3)  #Задаємо вектори
y = Vector(4,4,4)

print(x)
print(y)

print(f"Сума векторів х і у: {x+y}")
print(f"Різниця векторів х і у: {x-y}")

x.readfromtxt('1.txt')  #Міняємо значення вектора на значення з txt файлу

print(f"Змінене значення вектора х: {x}")

x.writeToTxt('2.txt')