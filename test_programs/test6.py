from tkinter import N
from tkinter.messagebox import NO
from xml.dom.minidom import Element


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        litr = ''
        itr = self.head
        while itr:
            litr += str(itr.data) + "-->"
            itr = itr.next
        print(litr)

    def insert_values(self, list):
        for element in list:
            self.insert_at_end(element)


    def get_length(self):
        ll = self.head
        count = 0
        while ll:
            count += 1
            ll = ll.next
        return count


    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise "invalid index"
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        elif index == 0:
            self.insert_at_beginning(data)
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = Node(data, itr.next)
                    break
                itr = itr.next
                count += 1


    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                return
            itr = itr.next


    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        else:
            print(f"element {data} not found")


ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.remove_at(2)
ll.print()
# ll.insert_after_value("mango","apple") # insert apple after mango
# ll.print()
# ll.remove_by_value("orange") # remove orange from linked list
# ll.print()
# ll.remove_by_value("figs")
# ll.print()
# ll.remove_by_value("banana")
# ll.remove_by_value("mango")
# ll.remove_by_value("apple")
# ll.remove_by_value("grapes")
# ll.print()