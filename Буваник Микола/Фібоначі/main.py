class InvalidValue(Exception):
    pass


def fibonachi(count_step=0, first_fibonachi=0, second_fibonachi=1):
    if count_step == 0:
        return first_fibonachi
    if count_step == 1:
        return second_fibonachi
    else:
        return (fibonachi(count_step - 1, first_fibonachi, second_fibonachi)
                + fibonachi(count_step - 2, first_fibonachi, second_fibonachi))


first_fibonachi = int(input("Input first fibonachi = "))
second_fibonachi = int(input("Input second fibonachi = "))
step = int(input("Input count step = "))
file_result = open("result.txt", 'a')
try:
    if step < 0:
        raise InvalidValue("Input negative count step")
    else:
        result = str(first_fibonachi) + "," + str(second_fibonachi)
        for iterator in range(2, step + 2):
            result += str("," + str(fibonachi(iterator, first_fibonachi, second_fibonachi)))
        print(result)
        file_result.write(result + "\n")
except InvalidValue as error:
    file_result.write("Error:" + str(error) + '\n')
    print("Error:" + str(error))
