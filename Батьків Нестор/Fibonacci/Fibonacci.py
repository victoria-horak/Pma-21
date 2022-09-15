
class NegativeLength(Exception):
    """Raised when the input length is negative"""


def fibonachi(first=0, second=1, length=1, fibonachi_line=""):
    if length < 0:
        raise NegativeLength("Length cannot be negative")
    if (len(fibonachi_line) == 0):
        fibonachi_line += str(first) + ", "
        fibonachi_line += str(second) + ", "
    next_num = first + second
    fibonachi_line += str(next_num) + ", "
    return fibonachi(second, next_num, length-1, fibonachi_line) if length > 1 else fibonachi_line[:-2]


try:
    print(fibonachi(0, 3, 4), "\n")
    print(fibonachi(0, 1, -2))
except NegativeLength as e:
    print(e)
