from ArrayList import ArrayList

try:
    array = ArrayList[int]()
    array.add(3)
    array.add(2)
    array.add(4)
    array.add(1)
    print(array)
    array.sort()
    print(array)
    array = array.insert(1, 5)
    array = array.replace(0, 100)
    array.pop()
    array = array.reverse()
    print(array)
except Exception as e:
    print(str(e))