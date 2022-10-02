class invalidLength(Exception):
    """Raised when step is negative"""


def fib(step=0, var1=0, var2=1):
     if step < 0:
         raise invalidLength("Length cannot be negative")
     elif step == 0:
         return var1
     else:
        return (fib(step - 1, var1, var2)) + (fib(step - 2, var1, var2))


step = int(input("input amount of numbers "))
var1 = int(input("input 1st number "))
var2 = int(input("input 2nd number "))
fibLine = ""
for i in range(0, step):
        result = var1 + var2
        var1 = var2
        var2 = result
        fibLine += str(result) + " "
print(fibLine)

