# Definition for singly-linked list.
from hashlib import new
from os import sep


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head
        
        count = 1
        node = head
        new_list = cur = ListNode()
        last_part = None
        array = []
        while node:
            if count < left:
                new_list.next = node
                new_list = new_list.next
            elif count >= left and count <= right:
                array.insert(0, node.val)
            else:
                last_part = node
                break
            node = node.next
            count += 1
        for i in array:
            new_list.next = ListNode(i, None)
            new_list = new_list.next
        if last_part:
            new_list.next = last_part
        return cur.next
        

    def print(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list


l11 = ListNode(5)
l12 = ListNode(4, l11)
l13 = ListNode(3, l12)
l14 = ListNode(2, l13)
l15 = ListNode(1, l14)

s = Solution()
l3 = s.reverseBetween(l15, 2, 4)

print(s.print(l3))