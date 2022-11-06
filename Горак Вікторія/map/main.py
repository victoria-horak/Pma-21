file = open('text.txt', 'r')
element = file.read().split('\n')
thisdict = {}
for i in range(len(element)):
    pairs = element[i].split()
    thisdict.update({pairs[0]: pairs[1]})

key = input('Enter the name of element: ')
if key not in thisdict.keys():
    print('There is no such key')
else:
    print(thisdict[key])
name = input('input element: ')
k = 0
for i in thisdict.keys():
    if thisdict[i] == name:
        print(i)
        k += 1

if k == 0:
    print('No key that have this element ')
