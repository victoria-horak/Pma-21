from IndexError import IndexError


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None


    def print(self):
        if self.head is None:
            print("your linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = new_node
            new_node.prev = itr
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def clear(self):
        self.head = None

    def insert_values(self, data_list):
        # self.head = None
        for data in data_list:
            self.append(data)

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise IndexError("index is out of length\n")
        if index == 0:
            self.head.prev = self.head
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.prev = itr.next
                break
            itr = itr.next
            count += 1


    def searchNode(self, value):
        i = 1
        flag = False
        # Node current will point to head
        current = self.head

        # Checks whether the list is empty
        if self.head is None:
            print("List is empty")
            return

        while current != None:
            # Compare value to be searched with each node in the list
            if current.data == value:
                flag = True
                break
            current = current.next
            i = i + 1

        if flag:
            print("Node is present in the list at the position : " + str(i))
        else:
            print("Node is not present in the list")




    def push_at(self, newElement, position):
        newNode = Node(newElement)
        if (position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1):
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, position ):
                if (temp != None):
                    temp = temp.next
            if (temp != None):
                newNode.next = temp.next
                newNode.prev = temp
                temp.next = newNode
                if (newNode.next != None):
                    newNode.next.prev = newNode
            else:
                print("\nThe previous node is null.")


    def pop_all(self, key):
        # 1. if the head is not null and value stored at head
        #   is equal to key, keep on adjusting the head as
        #   head next, delete previous head and adjust links
        #   until new head becomes null or not equal to key
        while (self.head != None and self.head.data == key):
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None
            if (self.head != None):
                self.head.prev = None

        # 2. create a temp node to traverse through the
        #   list and delete nodes with value equal to
        #   key and adjust links accordingly
        temp = self.head
        if (temp != None):
            while (temp.next != None):
                if (temp.next.data == key):
                    nodeToDelete = temp.next
                    temp.next = temp.next.next
                    if (temp.next != None):
                        temp.next.prev = temp
                    nodeToDelete = None
                else:
                    temp = temp.next