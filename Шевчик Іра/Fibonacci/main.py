class InvalidValue(Exception):
    pass

def fibonachi(count_step=0, fib1=0, fib2=1):
    if count_step == 0:
        return fib1
    if count_step == 1:
        return fib2
    else:
        return (fibonachi(count_step - 1, fib1, fib2)
                + fibonachi(count_step - 2, fib1, fib2))

n1 = 0;
n2 = 1;

answer = int(input("Default version 1 - yes; any other - no = "))

if answer == 1 :
    fib1 = n1
    fib2 = n2
    step = int(input("Count step = "))
    file_result = open("result.txt", 'a')
    try:
        if step < 0:
            raise InvalidValue("Input negative count step")
        else:
            result = str(fib1) + "," + str(fib2)
            for iterator in range(2, step + 2):
                result += str("," + str(fibonachi(iterator, fib1, fib2)))
            file_result.write(result + "\n")

    except InvalidValue as error:
        file_result.write("Error:" + str(error) + '\n')
else:
        fib1 = int(input("First fibonachi = "))
        fib2 = int(input("Second fibonachi = "))
        step = int(input("Count step = "))
        file_result = open("result.txt", 'a')
try:
    if step < 0:
        raise InvalidValue("Input negative count step")
    else:
        result = str(fib1) + "," + str(fib2)
        for iterator in range(2, step + 2):
            result += str("," + str(fibonachi(iterator, fib1, fib2)))
        print(result)
        file_result.write(result + "\n")

except InvalidValue as error:
    file_result.write("Error:" + str(error) + '\n')
    print("Error:" + str(error))
