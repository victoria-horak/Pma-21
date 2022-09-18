file_name = open('fibonacciError.txt','a+')
def fibonacci(first_number =0 , second_number = 1, steps = 3):
	
	if steps <= 0:
		return second_number
	else:
		print(first_number + second_number , end=" ")
		return fibonacci(second_number, first_number + second_number , steps-1)

def print_fibonacci(first_number,second_number,steps):
	
	print(first_number,second_number,end = " ")
	fibonacci_n = first_number + second_number
	first_number = second_number
	second_number = fibonacci_n
	print(fibonacci_n,end = " ")
	fibonacci(first_number,second_number,steps)
	print("\n")

first_number = int(input("Input first number = ")) 
second_number = int(input("Input second number =  "))

while True:
	try:
		steps = int(input("Input steps = "))
		assert steps >= 0
		break
	except AssertionError:
		file_name.write(("Steps cannot be negative number ")+ "\n")
		continue
		
print_fibonacci(first_number,second_number,steps)
print_fibonacci(first_number,second_number,7)
