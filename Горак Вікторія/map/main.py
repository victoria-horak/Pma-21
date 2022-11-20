file = open('text.txt', 'r')
element = file.read().split('\n')
thisdict = {None: "Ka", "Be": None}
for i in range(len(element)):
    pairs = element[i].split()
    thisdict.update({pairs[0]: pairs[1]})
thisdict.pop(None, None)
key = input('Enter the element: ')

if key not in thisdict.keys():
    print('There is no such key')
else:
    print(thisdict[key])
name = input('input the name of element: ')
element_count_in_dict = 0
for i in thisdict.keys():
    if thisdict[i] == name:
        print(i)
        element_count_in_dict += 1

if element_count_in_dict == 0:
    print('No key that have this element ')
