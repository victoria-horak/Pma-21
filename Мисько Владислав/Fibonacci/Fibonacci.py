def FibonacciNumber(n, first=0, second=1):
    if (n == 0): return first
    elif (n == 1): return second
    return FibonacciNumber(n - 1, first, second) + FibonacciNumber(n - 2, first, second)

result = open("result.txt", "w")

try: 
    n = int(input('Enter n: '))
    if (n < 0): 
        raise Exception
except Exception:
    result.write('Value is invalid')
    print('Value is invalid')
    result.close()
    exit()

firstNumber = int(input('Enter first value: '))
secondNumber = int(input('Enter second value: '))

fibonacciRow = []

for iterator in range(0, n + 1):
    fibonacciRow.append(FibonacciNumber(iterator, firstNumber, secondNumber))
print(fibonacciRow)

result.write('Resulting row: ')
result.write(''.join(str(x) + ' ' for x in fibonacciRow))
result.close()


