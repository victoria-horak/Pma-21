class IncorrectLength(Exception):
    """If the number of steps for fibonacci sequence is less than or equal to 0"""


# *args allows to pass a variable number of (non-keyword) arguments to a function
def fibonacci(*args):
    sequence = ""

    # if only the length is passed
    if len(args) == 1:
        element1 = 0
        element2 = 1
        steps = args[0]

    # if the first two numbers and the length are passed
    elif len(args) == 3:
        element1 = args[0]
        element2 = args[1]
        steps = args[2]

    else:
        element1 = args[0]
        element2 = args[1]
        steps = args[2]
        sequence = args[3]

    if steps < 0:
        raise IncorrectLength("Length <= 0")

    # if the sequence is empty, add the first two elements
    if len(sequence) == 0:
        sequence += str(element1) + " " + str(element2) + " "
    # keep adding next elements
    sequence += str(element1 + element2) + " "

    if steps == 1:
        # return first three elements
        return sequence
    else:
        # all other elements using recursion
        return fibonacci(element2, element1 + element2, steps - 1, sequence)


# user input:
first_element = int(input("First: "))
second_element = int(input("Second: "))
number_of_steps = int(input("Steps: "))

# print result:
try:
    print(fibonacci(first_element, second_element, number_of_steps))
except IncorrectLength as error:
    print(error)

# write into file:
file = open('fibonacci.txt', 'w')
try:
    file.write(str(fibonacci(first_element, second_element, number_of_steps)) + ' ')
except IncorrectLength as error:
    file.write(str(error))
file.close()
