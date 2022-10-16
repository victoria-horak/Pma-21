from LinkedList import LinkedList
from IndexError import IndexError

try:
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()
    linked_list1.insert_at_beginning(34)
    linked_list1.insert_at_beginning(9)
    linked_list1.insert_at_and(67)
    print("length ", linked_list1.get_length())
    linked_list1.print()

    # linked_list2.insert_values(["Kolia", "Lily", "Yura", "Vetal"])
    # linked_list2.remove_at(0)
    # linked_list2.insert_at_beginning(34)
    # linked_list2.insert_at(0, "Ann")
    # linked_list2.print()
except Exception as e:
    print(str(e))
