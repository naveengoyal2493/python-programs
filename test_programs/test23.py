# Definition for singly-linked list.
# from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def get_size(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def removeNthFromEnd(self, head: ListNode, n: int) ->ListNode:
        size = self.get_size(head)
        if size == 1 and n == 1:
            return ListNode("", None)
        if size > 1:
            till_count = size - n
            count = 1
            node = head
            while node:
                if count == till_count:
                    node.next = node.next.next
                    break
                node = node.next
                count += 1
            return head


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

l21 = ListNode(5)
l22 = ListNode(4, l21)
l23 = ListNode(3, l22)
l24 = ListNode(2, l23)
l25 = ListNode(1, l24)
# s = Solution()
# node = s.removeNthFromEnd(l5, 2)
# print(s.print(node))

class Solution2:
    # def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    #     cur = dummy = ListNode()
    #     while list1 and list2:               
    #         if list1.val < list2.val:
    #             cur.next = list1
    #             list1, cur = list1.next, list1
    #         else:
    #             cur.next = list2
    #             list2, cur = list2.next, list2
                
    #     if list1 or list2:
    #         cur.next = list1 if list1 else list2
            
    #     return dummy.next

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        return dummy.next

    def print(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list

s = Solution2()
l3 = s.mergeTwoLists(l15, l25)

print(s.print(l3))