from tkinter.messagebox import NO


class Node:

    def __init__(self, previous, data, next):
        self.previous = previous
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
        else:
            self.head = Node(None, data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(None, data, None)

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(self.head, data, None)

    def find_length(self):
        if self.head is None:
            print("Linked list is empty")
            return
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count
        
    def insert_by_index(self, index, data):
        if index < 0 or index >= self.find_length():
            raise Exception("invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        itr = self.head
        count = 0
        while itr.next:
            if count == index - 1:
                itr = Node(itr.previous,data,itr.next)
                break
            itr = itr.next
            count += 1

    def print_previous(self):
        if self.head is None:
            print("Linked list is empty")
            return
        litr = ''
        itr = self.head
        while itr:
            litr += "<--" + str(itr.data) + "-->"
            itr = itr.next
        print(litr)


ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)
ll.insert_at_beginning(3)
ll.insert_at_end(5)
print(ll.find_length())
ll.insert_by_index(2, 6)
ll.print_previous()
