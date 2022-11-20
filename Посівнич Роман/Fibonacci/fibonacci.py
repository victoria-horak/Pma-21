class IncorrectNumber(Exception):
    pass


def FibonacciNumber(number= 0, first=0, second=1):
    if number == 0: return first
    elif number == 1: return second
    return (FibonacciNumber(number - 1, first, second)
            + FibonacciNumber(number - 2, first, second))


try:
    file = open("fibonacci.txt", 'a')
    numberOfSteps = int(input("Input number of steps:"))
    firstNumber = int(input("Input first value:"))
    secondNumber = int(input("Input second value:"))

    if numberOfSteps < 0:
        raise IncorrectNumber("Number of steps < 0")
    else:
        for iterator in range(0, numberOfSteps + 2):
            print(FibonacciNumber(iterator, firstNumber, secondNumber))

except IncorrectNumber as t:
    print(t)
    file.write("Error, number of steps < 0")
