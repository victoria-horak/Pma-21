def get_name_by_symbol(chemical_elements: dict, symbol_to_look_for: str):
    for name, symbol in chemical_elements.items():
        if symbol == symbol_to_look_for:
            return name
    return "Such symbol is not present in the dictionary"

chemical_elements = {
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

flag = 1
while flag:
    print('Input chemical element to look for: ')
    element_to_look_for = input()
    try:
        print(chemical_elements[element_to_look_for])
    except Exception:
        print('Such key is not present in dictionary')
    finally:
        print('Want to continue? (0 - No, 1 - Yes): ')
        flag = int(input()) 

flag = 1
while flag:
    print('Input symbol of chemical element: ')
    symbol = input()
    print(get_name_by_symbol(chemical_elements, symbol))
    print('Want to continue? (0 - No, 1 - Yes): ')
    flag = int(input()) 