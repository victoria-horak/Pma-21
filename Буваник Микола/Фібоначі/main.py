from InvalidValueException import InvalidValueException


def fibonacci(count_step=0, first_fibonacci=0, second_fibonacci=1):
    if count_step == 0:
        return first_fibonacci
    if count_step == 1:
        return second_fibonacci
    else:
        return (fibonacci(count_step - 1, first_fibonacci, second_fibonacci)
                + fibonacci(count_step - 2, first_fibonacci, second_fibonacci))


try:
    first_fibonacci = int(input("Input first fibonacci = "))
    second_fibonacci = int(input("Input second fibonacci = "))
    step = int(input("Input count step = "))
    if step < 0:
        raise InvalidValueException("Input negative count step")
    else:
        result = str(first_fibonacci) + "," + str(second_fibonacci)
        for iterator in range(2, step + 2):
            result += str("," + str(fibonacci(iterator, first_fibonacci, second_fibonacci)))
        print(result)
        file_result = open("result.txt", 'a')
        file_result.write(result + "\n")
        file_result.close()
except InvalidValueException as error:
    file_result = open("result.txt", 'a')
    file_result.write("Error:" + str(error) + '\n')
    file_result.close()
    print("Error:" + str(error))
