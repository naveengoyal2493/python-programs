class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev


l11 = ListNode(5)
l12 = ListNode(4, l11)
l13 = ListNode(3, l12)
l14 = ListNode(2, l13)
l15 = ListNode(1, l14)

print(Solution().reverseList(l15).val)