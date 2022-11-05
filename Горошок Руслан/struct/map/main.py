def read_file(name_file):

    chemical_elements = {}

    with open(name_file, "r", encoding="utf8") as file:
        lines = file.readlines()
        for line in lines:
            first_elem, second_elem = line.split(" ")
            first_elem = first_elem.replace("\n", "")
            second_elem = second_elem.replace("\n", "")
            chemical_elements[first_elem] = second_elem
    return chemical_elements


file_name = "sources//data.txt"
chemical_element = read_file(file_name)
print(chemical_element)

name_of_the_element = input("Enter the name of the element (to display the designation of this element): ")
if name_of_the_element in chemical_element.keys():
    print(chemical_element[name_of_the_element])
else:
    print("Unfortunately, this item is not on the dictionary")

designation_of_the_element = input(
    "Enter the designation of the element (in order to find out if the name of this element is in the dictionary: "
    ).capitalize()

if designation_of_the_element in chemical_element.values():
    for name_element, designation_element in chemical_element.items():
        if designation_of_the_element == designation_element:
            print(name_element)
            break
else:
    print("Unfortunately, this item is not on the dictionary")
