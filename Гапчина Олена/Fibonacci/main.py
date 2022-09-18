def fibonacci(steps=0, first_number=0, second_number=1):
    if steps == 0:
        return first_number
    elif steps == 1:
        return second_number
    else:
        return fibonacci(steps - 1, first_number, second_number) + fibonacci(steps - 2, first_number, second_number)


num_of_steps = int(input("Number of steps: "))
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

for i in range(num_of_steps + 2):
    print(fibonacci(i, num1, num2))
