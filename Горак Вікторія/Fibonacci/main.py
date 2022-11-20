from Exception import *


def fibonacci(*args):
    if len(args) == 1:
        first = 0
        second = 1
        length = args[0]
        line = ""
    elif len(args) == 3:
        first = args[0]
        second = args[1]
        length = args[2]
        line = ""
    else:
        first = args[0]
        second = args[1]
        length = args[2]
        line = args[3]

    if length < 0:
        raise WrongLength("Length is less than zero")
    if len(line) == 0:
        line += str(first) + ", " + str(second) + ", "
    next_fib = first + second
    line += str(next_fib) + ", "
    return fibonacci(second, next_fib, length - 1, line) if length > 1 else line


file = open('text.txt', 'w')
try:
    print(fibonacci(0, 1, 4), "\n")
    print(fibonacci(3, 4, 1))
except WrongLength as error:
    print(error)
    file.write(str(error))
    file.close()
