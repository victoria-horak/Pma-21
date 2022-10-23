from arrayList.ArrayList import ArrayList

file_name = "D:\\Python\\ClassArrayList\\sources\\FirstArrayList"
print("Create array_list")
array_list = ArrayList(14, 10, 6, 0, 5, 2, 10, 7, 0, 6, 5)
print(array_list)

print("\nAdd one element to array_list")
array_list.add_one_element(7)
print(array_list)

print("\nAdd more element to array_list")
array_list.add_more_element(4, 14, 6, 8, 2)
print(array_list)

print("\nRemove one element from array_list")
array_list.remove_one_element(8)
print(array_list)

print("\nRemove all enter this element from array_list")
array_list.remove_all_enter_element(7)
print(array_list)

print("\nRemove last enter this element from array_list")
array_list.remove_last_enter_element(14)
print(array_list)

print("\nRemove more element from array_list")
array_list.remove_more_element(2, 4)
print(array_list)

print("\nRemove all enter more element from array_list")
array_list.remove_all_enter_elements(0, 6)
print(array_list)

print("\nRemove last enter more element from array_list")
array_list.remove_last_enter_elements(10, 5)
print(array_list)

print("Iterator ArrayList")
it = array_list.get_iterator()
while it.has_next():
    print(it.next(), end=" ")
