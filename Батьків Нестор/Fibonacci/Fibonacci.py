
class NegativeLength(Exception):
    """Raised when the input length is negative"""


PATH = './Батьків Нестор/Fibonacci/'


def fibonachi_internal(first, second, length, fibonachi_line=""):
    if length < 0:
        raise NegativeLength("Length cannot be negative")
    if (len(fibonachi_line) == 0):
        fibonachi_line += str(first) + ", "
        fibonachi_line += str(second) + ", "
    next_num = first + second
    fibonachi_line += str(next_num) + ", "
    return fibonachi_internal(second, next_num, length-1, fibonachi_line) if length > 1 else fibonachi_line[:-2]


def add_to_file(text):
    file = open(PATH+"result.txt", "a")
    file.write(str(text) + "\n")
    file.close()


def fibonachi(first=0, second=1, length=1):
    try:
        result = fibonachi_internal(first, second, length)
        print(result)
        add_to_file(result)
    except NegativeLength as error:
        print(error)
        add_to_file(error)


fibonachi(1, 0, 3)
fibonachi(-2, 5, -2)
fibonachi(7, 12, 14)
fibonachi(7, 16, 35)
