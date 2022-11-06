

from classArrayList import Arraylist

print ("cтворюємо обʼєкт класу Arraylist ")
x = Arraylist([7,8,9,10,7])
print(x)

print("Читаємо дані з файлу ")
file1 = open("matr1.txt", "r")
x.read_from_file(file1)
print (x)

print("Додаємо один елемент")
x.add_element(25)
print(x)

print("Додаємо пару елементів")
x.add_elements(25,30,10)
print (x)

print("Видаляєм зі списку обʼєкт за значенням ")
x.remove_element(10)
print(x)

print("Видаляєм зі списку пару обʼєктів за значенням ")
x.remove_elements(25,7)
print(x)
