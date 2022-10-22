from LinkedList import LinkedList

lst = LinkedList[int]()
lst.initial_insert(3)
lst.insert_after_element(3, 53)
lst.insert_before_element(53, 1)
lst.insert_at_end(25)
lst.insert_at_beginning(255)
print(lst)
lst.reverse()
print(lst)
