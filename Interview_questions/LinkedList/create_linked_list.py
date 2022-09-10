class ListNode:

    def __init__(self, val, next):
        self.val = val
        self.next = next
  
class LinkedList:

    @staticmethod
    def insert_at_beginning(val, head = None):
        return ListNode(val, head)        

    @staticmethod
    def insert_values(values, head = None):
        for i in range(len(values) - 1, -1, -1):
            head = LinkedList.insert_at_beginning(values[i], head)
        return head

    @staticmethod
    def merge_two_linked_lists(firsthead, lasthead):
        itr = firsthead
        while itr.next:
            itr = itr.next
        itr.next = lasthead
        return firsthead
    
    @staticmethod
    def print_ll(head):
        if not head:
            return "Linked list is empty"
        itr = head
        ll = ""
        while itr:
            ll += str(itr.val) + "-->"
            itr = itr.next

        print(ll)


class TwoPointerListNode:

    def __init__(self, val, next=None, bottom=None):
        self.val = val
        self.next = next
        self.bottom = bottom

class NextAndRandomListNode:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random