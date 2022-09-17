class InvalidData(Exception):
    pass


def fibonachi(end_number=0, first_number=0, second_number=1):
    if end_number == 0:
        return first_number
    if end_number == 1:
        return second_number
    else:
        return (fibonachi(end_number - 1, first_number, second_number)
                + fibonachi(end_number - 2, first_number, second_number))


first = int(input("First numeric of fibonachi = "))
second = int(input("Second numeric of fibonachi = "))
last = int(input("Last number fibonachi = "))
file = open("exception.txt", 'a')

try:
    if last < 0:
        raise InvalidData("You input incorrect data")
    for iterator in range(0, last + 2):
        print(fibonachi(iterator,first,second))
except InvalidData as e:
    file.write(str(e) + '\n')
    print(e)
file.close()
