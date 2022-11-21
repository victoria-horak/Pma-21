from NegativeLength import NegativeLength


def fibonachi(count=0, firstNum=0, secondNum=1):
    if count == 0:
        return firstNum
    if count == 1:
        return secondNum

    else:
        return (fibonachi(count - 1, firstNum, secondNum) + fibonachi(count - 2, firstNum, secondNum))


count = int(input("Cont of numbers fibonachi = "))
first_fibonaci = int(input("First numeric of fibonachi = "))
second_fibonaci = int(input("Second numeric of fibonachi = "))

try:
    if count < 0:
        raise NegativeLength("count of numbers is negative")
    else:
        for length in range(count + 2):
            print(fibonachi(length, first_fibonaci, second_fibonaci))
except NegativeLength as e:
    file = open("error.txt", "a")
    print(e)
    file.write("\n Error----count is negative----")
    file.close()