def fibonachi(count=0, firstNum = 0, secondNum = 1):
    if count == 0:
        return firstNum
    if count == 1:
        return secondNum

    else:
        return(fibonachi(count-1, firstNum,secondNum)+fibonachi(count-2,firstNum,secondNum))


count = int(input("Cont of numbers fibonachi = "))
first = int(input("First numeric of fibonachi = "))
second = int(input("Second numeric of fibonachi = "))


class NegativeLength(Exception):
    pass

try:
    if count < 0:
        file = open("error.txt", "a")
        raise NegativeLength("count of numbers is negative")
    else:
        for length in range(count + 2):
            print(fibonachi(length,first, second))
except NegativeLength as e:
    print(e)
    file.write("\n Error----count is negative----")

