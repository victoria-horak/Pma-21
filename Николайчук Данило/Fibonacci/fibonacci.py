#fibonacci method with regursion
class LessThanZero(Exception):
    "Raise when number person enter is less than zero"
    pass

def fibonacci(number, firstNumber = 0, secondNumber = 1):
    if number > 1:
        print(firstNumber + secondNumber, end="\t")
        file.write(str(firstNumber + secondNumber)+"\t")
        return fibonacci(number-1, secondNumber, firstNumber+secondNumber)
    file.write(str(firstNumber + secondNumber)+"\n")
    return firstNumber+secondNumber

try:
    file = open("fibonacciDate.txt", "a")
    number = int(input("Enter number: "))
    if number < 1:
        raise LessThanZero
    print(fibonacci(number))
except LessThanZero:
    file.write("It is impossible to count a negative number of operations.\n")
    print("It is impossible to count a negative number of operations.")
except ValueError as exc:
    file.write(str(exc)+"\n")
    print("You have entered incorrect data (the program cannot convert characters into numbers).")
except:
    file.write("Error.\n")
    print("Error.")
finally:
    file.close()