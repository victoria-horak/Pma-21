class IncorrectNumber:
    pass


def FibonacciNumber(number=0, first=0, second=1):
    if number == 0:
        return first
    if number == 1:
        return second
    else:
        return (FibonacciNumber(number - 1, first, second)
                + FibonacciNumber(number - 2, first, second))


numberOfSteps = int(input("Input number of steps:"))
firstNumber = int(input("Input first value:"))
secondNumber = int(input("Input second value:"))

file = open("text.txt", 'r')

try:
    if numberOfSteps < 0:
        raise IncorrectNumber("Count < 0")
    else:
        for iterator in range(0, numberOfSteps + 2):
            print(FibonacciNumber(iterator, firstNumber, secondNumber))
except IncorrectNumber as r:
    file.write('Count < 0')
    print(r)
file.close()
