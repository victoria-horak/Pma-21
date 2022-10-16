from ArraList import ArrayList
from ExceptionsIsElement import ExceptionIsElementPresent

list = [1, 6, 4, 3, 6, 4]
array_list = ArrayList(list)
array_list.append_to_ArrayList(2)
print('Append\n' + str(array_list))
array_list.pop_from_list(0)
print('Pop\n' + str(array_list))
array_list.if_element_present(3)

try:

    array_list.insert(11, 5)
    print('Insert\n' + str(array_list))


except ExceptionIsElementPresent as ex:
    print(ex)
array_list.reverse()
print('Reverse\n' + str(array_list))
array_list.sotr_array()
print('Sort\n' + str(array_list))
array_list.clear_of_elements()
print('Clear\n' + str(array_list))
