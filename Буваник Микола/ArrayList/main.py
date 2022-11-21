from ArrayList import ArrayList

try:
    a = ArrayList([2])
    print("Your ArrayList: ", a, len(a))
    a.append([3, 2, 2, 5])
    print(a, len(a))
    a.pop(1)
    print(a, len(a))
    a.remove(6)
    print(a, len(a))
    a.insert([4, 4], 3)
    print(a, len(a))
    a.remove(2)
    print(a, len(a))
    a.clear()
    print(a, len(a))
except Exception as e:
    print(str(e))
    with open("Result.txt", "a") as file:
        file.write(str(e) + "\n")
