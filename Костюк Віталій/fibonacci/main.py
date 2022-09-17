class NegativeLastNumber(Exception):
    pass

def fibonacci(first, second, last):
    if last == 0: return first
    if last == 1: return second
    else: return (fibonacci(first, second, last - 1) + fibonacci(first, second, last - 2))

file = open("exc.txt", 'a')

first_str = input("Перше число алгоритму Фібоначчі = ")
second_str = input("Друге число алгоритму Фібоначчі = ")
last_str = input("Номер числа Фібоначчі, яке треба знайти = ")
if first_str == '':
    first = 0
else:
    first = int(first_str)
if second_str == '':
    second = 1
else:
    second = int(second_str)
if last_str == '':
    last = 0
else:
    last = int(last_str)
try:
    if last < 0:
        raise NegativeLastNumber("Numeric can`t be negative")
    for iterator in range(0, last + 2):
        print(fibonacci(first, second, iterator))
except NegativeLastNumber as e:
    print(e)
    file.write(str(e) + '\n')
file.close()