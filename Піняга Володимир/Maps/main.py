from functions import *


chemistry_elements = read_from_file("elements.txt")
print("ELEMENTS: ")
print(chemistry_elements)

name = input("Enter name of the element: ")
find_name(chemistry_elements, name)
print("========================")
mark = input("Enter mark of element: ")
find_mark(chemistry_elements, mark)
