# (1) input a dictionary from file
dictionary = {}
with open("elements.txt") as file:
    for line in file:
        (key, value) = line.split()
        if key == "None" or value == "None":
            continue
        dictionary[key] = value
dictionary.update({'Calcium': 'Ca'})

# (2) print a dictionary
print("Dictionary:")
for name, symbol in dictionary.items():
    print(f'{name} - {symbol}')

# (3) find symbol of the element by its name
def find_by_name(dictionary_name):
    searched_name = input("\nEnter a name of the element you want to find: ")
    if searched_name not in dictionary_name.keys():
        print("The element was not found.")
    else:
        for element_name, element_symbol in dictionary_name.items():
            if element_name == searched_name:
                print(f'The symbol for {element_name} is {element_symbol}.')


# (4) find name of the element by its symbol
def find_by_symbol(dictionary_name):
    searched_symbol = input("\nEnter a symbol of the element you want to find: ")
    if searched_symbol not in dictionary_name.values():
        print("The element was not found.")
    else:
        for element_name, element_symbol in dictionary_name.items():
            if element_name == searched_symbol:
                print(f'The symbol for {element_symbol} is {element_name}.')
                

find_by_name(dictionary)
find_by_symbol(dictionary)
