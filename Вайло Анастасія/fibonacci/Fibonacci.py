def Fibo(n, first_element=0,second_element=1):
    if n == 0: return first_element
    elif n == 1: return second_element
    return Fibo(n - 1, first_element, second_element) + Fibo(n - 2, first_element, second_element)
answer = open("fibonacci.txt", "w")
try: 
    n = int(input('input n: '))
    if (n < 0): 
        raise Exception
except Exception:
    answer.write('Value is invalid')
    print('n is less than zero')
    answer.close()
    exit()
firstNum = int(input('input first number: '))
secondNum = int(input('input second number: '))
fibonacci = []
for iterator in range(0, n + 1):
    fibonacci.append(Fibo(iterator, firstNum, secondNum))
print(fibonacci)
lineToFile = ''
for element in fibonacci:
    lineToFile += str(element) + ' '
answer.write(lineToFile)
answer.close()
