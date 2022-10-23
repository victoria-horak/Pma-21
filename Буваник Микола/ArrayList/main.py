from ArrayList import ArrayList

try:
    a = ArrayList([1, 4, 2, 4, 3])
    print("Your ArrayList: ",a)
    a.insert([10,11,12],4)
    print("Your ArrayList after insert: ",a)
    a.sort()
    print("Your ArrayList after sort: ",a)
    a.pop(5)
    print("Your ArrayList after pop element : ",a)
    a.append(13)
    print("Your ArrayList after append element: ",a)
    a.remove(4)
    print("Your ArrayList after remove 4: ",a)
except Exception as e:
    print(str(e))
    with open("Result.txt", "a") as file:
        file.write(str(e) + "\n")