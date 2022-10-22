from LinkedList import LinkedList
from Constants import PATH

result_file = PATH + "Result.txt"


def add_to_file(text, filePath=result_file):
    with open(filePath, "a") as file:
        file.write(f"\n{text}\n")


with open(result_file, "w") as file:
    file.write("")

arr = [6, 6, -2, -3]
arr2 = [5, 7, 6, 8, 9, -2]
mylist = LinkedList("2 3 4 5 6")
add_to_file("Linked list")
mylist.toFile(result_file)
add_to_file(f"Add {arr} to start: ")
mylist.insert_at_start(*arr).toFile(result_file)
add_to_file(f"Add {arr2} to end: ")
mylist.insert_at_end(*arr2).toFile(result_file)
add_to_file(f"remove 2 entries of 6:")
mylist.remove_entries(6, 2).toFile(result_file)
add_to_file(f"insert 1 at index:-2")
mylist.insert(-2, 1).toFile(result_file)
add_to_file(f"remove everything from 2 to -3")
mylist.remove(2, -3).toFile(result_file)
add_to_file(f"and reverse")
mylist.reverse().toFile(result_file)
