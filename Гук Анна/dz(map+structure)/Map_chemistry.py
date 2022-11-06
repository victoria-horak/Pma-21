from ExceptionNoElement import Exception_no_such_element
elements={
    "Litiy":"Li",
    "Beriliy":"Be",
    "Heliy":"He",
    "Aurum":"Au",
    "Kaliy":"K",
    "Vanadiy":"V",
    "Chrom":"Cr",
    "Ferum":"Fe"
}
print("The full list of elements:")
print(elements)

element_is_present_by_name=input("ENTER THE FULL NAME OF ELEMENT U WANT TO CHECK THE PRESENT IN LIST:")
if element_is_present_by_name in elements.keys():
    print(elements[element_is_present_by_name],"-abbreviation of the searched element")
else:
    # raise Exception_no_such_element("There is no such element!!")
    print("There is no such element!!")

element_is_present_by_abbreviation=input("ENTER THE ABBREVIATION U WANT TO CHECK THE PRESENT IN LIST:")
if element_is_present_by_abbreviation in elements.values():
    for full_name,abbreviation in elements.items():
        if element_is_present_by_abbreviation==abbreviation:
            print(full_name,"-the full name of this element")
else:
    print("There is no such element!!")