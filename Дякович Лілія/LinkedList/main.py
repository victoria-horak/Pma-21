from LinkedList import LinkedList
from IndexError import IndexError

# try:
#     linked_list1 = LinkedList()
#     linked_list2 = LinkedList()
#     linked_list1.insert_at_beginning(34)
#     linked_list1.insert_at_beginning(9)
#     linked_list1.insert_at_and(67)
#     print("length ", linked_list1.get_length())
#     linked_list1.print()
#
#     # linked_list2.insert_values(["Kolia", "Lily", "Yura", "Vetal"])
#     # linked_list2.remove_at(0)
#     # linked_list2.insert_at_beginning(34)
#     # linked_list2.insert_at(0, "Ann")
#     # linked_list2.print()
# except Exception as e:
#     print(str(e))


ll1 = LinkedList()
ll1.append(23)
ll1.append(24)
ll1.append(27)
ll1.append(26)
ll1.append(27)
ll1.prepend(27)
ll1.remove_at(3)
ll1.remove_at(2)
ll1.insert_values([23, 67, 89, 65, 45])
ll1.searchNode(23)
ll1.push_at(2,2)
# ll1.pop_all(27)
print(ll1.get_length())

ll1.print()

