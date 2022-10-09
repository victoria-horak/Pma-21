from datetime import datetime

class WrongFormat(Exception):
    pass

def Fibonacci(n = 0, first = 0, second = 1):
    if n == 0:
        return first
    if n == 1:
        return second
    return Fibonacci(n - 1, first, second) + Fibonacci(n - 2, first, second)

try:
    file = open("fibonacci.txt", "a")
    userInput = input("Enter in any format:\n[1] - stepsAmount firstNumber secondNumber\n[2] - stepsAmount\nEnter : ")
    if userInput.count(" ") != 0 and userInput.count(" ") != 2:
        raise WrongFormat("Wrong format of input")
    words = userInput.split(' ')
    for word in words:
        if not word.lstrip("-").isdigit():
            raise TypeError("Values have to be numeric")

    fibonacciSequence = []
    if int(words[0]) < 0:
        raise ValueError("Number cannot be negative")
    n = int(words[0])
    if len(words) == 1:
        for i in range(0, n + 2):
            fibonacciSequence.append(Fibonacci(i))
        print(fibonacciSequence)
    else:
        firstValue = int(words[1])
        secondValue = int(words[2])
        for i in range(0, n + 2):
            fibonacciSequence.append(Fibonacci(i, firstValue, secondValue))
        print(fibonacciSequence)
    file.write("[" + ", ".join(str(x) for x in fibonacciSequence) + "]\n")
except Exception as exc:
    file.write("[" + str(datetime.now()) + "] Error : " + str(exc) + '\n')
    print("Error occured : " + str(exc))
finally:
    file.close()
