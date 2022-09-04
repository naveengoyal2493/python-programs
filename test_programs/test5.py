
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_in_beginning(self, data):
        self.head = Node(data, self.head)
        
    def print(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        
        itrl = ''
        while self.head:
            itrl += str(self.head.data) + "-->"
            self.head = self.head.next
        print(itrl)


ll = LinkedList()
ll.insert_in_beginning(4)
ll.insert_in_beginning(5)
ll.print()