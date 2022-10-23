from ArrayList import ArrayList


result_file = './Батьків Нестор/arrayList/Result.txt'


def add_to_file(*sentences):
    with open(result_file, "a") as file:
        file.write("\n")
        for elem in sentences:
            file.write(f"{elem}\n")


with open(result_file, "w") as file:
    file.write("")


arList = ArrayList(1)
arList.add(2, 4, 5, 7, 2)
add_to_file("ArrayList:", arList)
add_to_file("add 1:", arList.add(1))
add_to_file("add [3,2,-2]:", arList.add(*[3, 2, -1]))
add_to_file("delete element with index: 2:", arList.delete(2))
add_to_file("delete element with index: -3:", arList.delete(-3))
add_to_file("count entries of 2:", arList.count(2))
add_to_file("reverse", arList.reverse())
add_to_file("remove 2 entries of 2:", arList.remove_entries(2, 2))
add_to_file("insert 'nestor' after index 1", arList.insert(2, *'nestor'))
