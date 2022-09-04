from os import link
from tkinter import N
from tkinter.messagebox import NO


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linklist is empty")
            return
        listr = ''
        itr = self.head
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)

link_list = LinkList()
link_list.insert_at_beginning(3)
link_list.insert_at_beginning(85)
link_list.print()