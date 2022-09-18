class IncorrectLength(Exception):
    """When length <= 0"""

def recursiveFibonacci(first = 0, second = 1, length = 10, end=""): #по замовчуванню
    if length <= 0:
        raise IncorrectLength("Length is less or equal 0")

    if (len(end) == 0):
        end += str(first) + " "
        end += str(second) + " "
    next = first + second #наступне після двох останніх - принцип алгоритму Фібоначчі
    end += str(next) + " "
    return recursiveFibonacci(second, next, length-1, end) if length > 1 else end[:-2]

file = open('file1.txt', 'r') #відкритти файл для читання
file = file.read()
numberList = (file.split(" ")) 

#блок винятків
try:
    print(recursiveFibonacci(int(numberList[0]),int(numberList[1]),int(numberList[2])))

except IncorrectLength as errorr:
    print(errorr)
    file=open('file1.txt', 'a') #вілкрити і додати у кінець файлу
    file.write("\nError - Length is less or equal 0")
    file.close()