from ArrayList import ArrayList

try:
    array = ArrayList[int]()
    array.add_item(3)
    print(array)
    array.sort()
    print(array)
    array = array.insert(1, 5)
    print(array)
    array = array.replace(0, 100)
    print(array)
    array.pop()
    print(array)
    array = array.reverse()
    print(array)
    array.clear()
    print(array)
except Exception as e:
    print(str(e))
