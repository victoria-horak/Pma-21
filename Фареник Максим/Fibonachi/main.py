def fibonachi(first=0, second=1, length=3, line=""):
    if length < 0:
        raise Exception("Length is less than 0")

    if (len(line) == 0):
        line += str(first) + ", "
        line += str(second) + ", "
    nextnumber = first + second
    line += str(nextnumber) + ", "
    return fibonachi(second, nextnumber, length-1, line) if length > 1 else line[:-2]

f=open('data.txt', 'r')
f = f.read()
num_array=(f.split(" "))

try:
    print(fibonachi(0, 1, 5))
    print(fibonachi(int(num_array[0]),int(num_array[1]),int(num_array[2])))

except Exception as e:
    print(e)
    f=open('data.txt', 'a')
    f.write("\nError - Length is less than 0")
    f.close()