class ValueLessThanZero(Exception):
    """This value can't be zero"""


def fibonachi(amountOfNumbers=1, firstNumber=0, secondNumber=1):
    if amountOfNumbers != 0:
        outputFile.write(str(firstNumber + secondNumber) + " ")
        return fibonachi(amountOfNumbers - 1, secondNumber, firstNumber + secondNumber)
    return firstNumber + secondNumber
    outputFile.write(str(firstNumber + secondNumber) + " ")


outputFile = open("output.txt", "w")
try:
    firstNumber = int(input("enter first number:"))
    secondNumber = int(input("enter second number:"))
    amountOfNumbers = int(input("enter amount number:"))
    if amountOfNumbers < 0:
        raise ValueLessThanZero
    outputFile.write(str(firstNumber) + " " + str(secondNumber) + " ")
    fibonachi(amountOfNumbers, firstNumber, secondNumber)
except ValueLessThanZero:
    outputFile.write("this value can't be zero")
    print("This value can't be zero")
except ValueError as errorMessage:
    outputFile.write(str(errorMessage))
    print("\n""Invalid value")
outputFile.close()

