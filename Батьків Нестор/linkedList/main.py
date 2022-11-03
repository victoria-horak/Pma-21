from LinkedList import LinkedList
from Constants import PATH

result_file = PATH + "Result.txt"


def add_to_file(text, filePath=result_file):
    print(text, end=" ")
    # with open(filePath, "a") as file:
    #     file.write(f"\n{text}\n")


with open(result_file, "w") as file:
    file.write("")


arr = [4, 4]
arr2 = [3, 2, 2]
mylist = LinkedList()
add_to_file("Linked list:")
print(mylist)
add_to_file(f"Add 2: ")
print(mylist.insert_at_end(2))
add_to_file(f"Add {arr2} : ")
print(mylist.insert_at_end(*arr2))
add_to_file(f"Add 2:")
print(mylist.insert_at_end(2))
add_to_file(f"remove at index 1:")
print(mylist.remove(1))
add_to_file(f"Add 3:")
print(mylist.insert_at_start(3))
add_to_file(f"remove 3:")
print(mylist.remove_entries(3))
add_to_file(f"remove alll 2:")
print(mylist.remove_entries(2, -1))
add_to_file(f"Add {arr} : ")
print(mylist.insert_at_end(*arr))
add_to_file(f"Clear  : ")
print(mylist.clear())
