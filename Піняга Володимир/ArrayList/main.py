from ClassArrayList import *

print("ARRAY LIST:")
array_list = ArrayList()
array_list.read_from_file("data.txt")
print(array_list)

print("\nNew Array List: ")
array_list.size()
print(array_list)

print("\nAdd one element to Array List: ")
array_list.append_one(7)
print(array_list)

print("\nAppend more element to Array List: ")
array_list.append_more(5, 17, 67, 2, 3, 10)
print(array_list)

print("\nRemove one element from Array List: ")
array_list.pop_one(6)
print(array_list)

print("\nRemove all entered this element from Array List: ")
array_list.pop_all_entered(14)
print(array_list)

print("\nRemove last entered this element from Array List: ")
array_list.pop_last_entered(5)
print(array_list)

print("\nRemove more elements from Array List: ")
array_list.pop_more(2, 3)
print(array_list)

print("\nRemove all entered more elements from Array List: ")
array_list.pop_all_entered_elements(8, 1)
print(array_list)

print("\nRemove last entered more elements from Array List: ")
array_list.pop_last_entered_elements(17, 67)
print(array_list)

print("Clear Array List: ")
array_list.clear()
