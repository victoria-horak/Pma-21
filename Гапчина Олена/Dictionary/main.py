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

# (3) find name of the element by its symbol
searched_name = input("\nEnter a name of the element you want to find: ")
if searched_name not in dictionary.keys():
    print("The element was not found.")
else:
    for name, symbol in dictionary.items():
        if name == searched_name:
            print(f'The symbol for {name} is {symbol}.')

# (4) find symbol of the element by its name
searched_symbol = input("\nEnter a symbol of the element you want to find: ")
if searched_symbol not in dictionary.values():
    print("The element was not found.")
else:
    for name, symbol in dictionary.items():
        if symbol == searched_symbol:
            print(f'The name for {symbol} is {name}.')
