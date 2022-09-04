class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    
    def __init__(self):
        self.head = None

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if not self.head:
            self.insert_at_beginning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, nums):
        for num in nums:
            self.insert_at_end(num)

    def printll(self):
        itr = self.head
        complete_string = ""
        while itr:
            complete_string += str(itr.data) + "-->"
            itr = itr.next
        print(complete_string)

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            return f"Invalid Index {index}"
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            count += 1
            itr = itr.next
        
    def insert_at(self, value, index):
        if index < 0 or index > self.get_length():
            return f"Invalid Index {index}"
        
        if index == 0:
            self.insert_at_beginning(value)
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(value, itr.next)
            count += 1
            itr = itr.next

    def insert_after_value(self, after_value, data):
        itr = self.head
        while itr:
            if itr.data == after_value:
                itr.next = Node(data, itr.next)
                return
            itr = itr.next
        return "Value not found"

    def remove_by_value(self, value_to_remove):
        itr = self.head
        while itr.next:
            if itr.next.data == value_to_remove:
                itr.next = itr.next.next
            itr = itr.next

ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert_values([6,7,8,9])
# ll.remove_at(8)
ll.insert_at("Figs", 5)
ll.insert_after_value("Figs", "lallu")
ll.remove_by_value(4)
ll.printll()

