f = open('fibonacci.txt')
f1 = open('result.txt', 'a')
fib1, fib2, numb = map(int, f.readline().split(","))


def fibonacci(numb=1, fib1=0, fib2=1):
    if numb < 0:
        f1.write('Numb should be bigger then 0'+"\n")
        raise (Exception('Numb should be bigger then 0'))

    fib = fib1 + fib2
    # print(fib)
    f1.write(str(fib)+' ')
    if 0 < numb:
        return fibonacci(numb-1, fib2, fib)
    return fib


fibonacci(numb, fib1, fib2)

f1.close()


