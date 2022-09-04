from create_linked_list import TwoPointerListNode, ListNode
# def mergeList(headA,headB):
#     fh=None
#     ft=None
#     while headA and headB:
#         print(headA.val)
#         print(headB.val)
#         if fh==None:
#             if headA.val<headB.val:
#                 fh=headA
#                 ft=headA
#                 headA=headA.bottom
#             else:
#                 fh=headB
#                 ft=headB
#                 headB=headB.bottom
#         else:
#             if headA.val<headB.val:
#                 ft.bottom=headA
#                 headA=headA.bottom
#                 ft=ft.bottom
#             else:
#                 ft.bottom=headB
#                 headB=headB.bottom
#                 ft=ft.bottom
                
                
#     if headA:
#         ft.bottom=headA
#     if headB:
#         ft.bottom=headB
    
#     return fh    

def merge_two_sorted_linked_list(head1, head2):
    itr = head3 = TwoPointerListNode(0)
    while head1 and head2:
        if head1.val < head2.val:
            itr.bottom = TwoPointerListNode(head1.val)
            head1 = head1.bottom
        else:
            itr.bottom = TwoPointerListNode(head2.val)
            head2 = head2.bottom
        itr = itr.bottom

    if head1:
        itr.bottom = head1
    
    if head2:
        itr.bottom = head2

    return head3.bottom

def flatten(root):
    #Your code here
    if root==None:
        return None
        
    if root.next==None:
        return root

    return merge_two_sorted_linked_list(root, flatten(root.next))

l1 = TwoPointerListNode(5)
l1.next = TwoPointerListNode(6)
l1.next.next = TwoPointerListNode(8)
l1.next.next.bottom = TwoPointerListNode(11)
l1.next.next.bottom.bottom = TwoPointerListNode(12)
l1.next.bottom = TwoPointerListNode(10)
l1.bottom = TwoPointerListNode(7)
l1.bottom.bottom = TwoPointerListNode(9)

head = flatten(l1)
while head:
    print(head.val)
    head = head.bottom