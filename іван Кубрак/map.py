chemical_elements={
    "Cuprum": "Cu",
    "Oxygen": "O",
    "Nitrogen" : "N",
    "Boron": "B",
    "Neon": "Ne",
    "Silicon": "Si",
    "Helium": "He",
    "Aluminium": "Al",
    "Carbon": "C",
    "Titanium": "Ti",
    "Calcium": "Ca"
}
print(chemical_elements)


element_mark=input("Input mark element:")
if element_mark in chemical_elements.values():
    for full_name,mark in chemical_elements.items():
        if element_mark==mark:
            print(full_name,"-the full name of this element")
else:
    print("This element not exist")

element_full_name=input("Input full name element:")
if element_full_name in chemical_elements.keys():
    print(chemical_elements[element_full_name],"-mark of this element")
else:
    print("This element not exist")






